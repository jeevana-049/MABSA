"""
MABSA demo: Explainable Multimodal Aspect-Based Sentiment Analysis.

Works in three modes:
  1) text only      python demo.py --text "..." --aspect "..."
  2) image only     python demo.py --image path/to/image.jpg
  3) text + image   python demo.py --text "..." --aspect "..." --image path/to/image.jpg

The trained model folder (default: ./mabsa_model) must be downloaded from Drive.
"""
import argparse
import re

import cv2
import easyocr
import torch
from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                          BlipForConditionalGeneration, BlipProcessor)

LABELS = ["negative", "neutral", "positive"]
STOP = set("a an the is of in on at to and with for this that it his her "
           "their its are was be by as from or up".split())


def words(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower())
            if w not in STOP and len(w) > 2}


def ocr_chunks(aspect, text, ocr):
    """Aspect-oriented filtration: keep only OCR pieces related to the aspect or tweet."""
    key = words(aspect) | words(text)
    w = ocr.split()
    chunks = [" ".join(w[i:i + 8]) for i in range(0, min(len(w), 64), 8)]
    return [c for c in chunks if words(c) & key]


def build_visual(cap, chunks):
    return (cap + " . " + " ".join(chunks)).strip()


class MABSA:
    def __init__(self, model_dir="mabsa_model"):
        self.dev = "cuda" if torch.cuda.is_available() else "cpu"
        print("Loading models on", self.dev, "...")
        self.tok = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_dir).to(self.dev).eval()
        name = "Salesforce/blip-image-captioning-base"
        self.proc = BlipProcessor.from_pretrained(name)
        self.blip = BlipForConditionalGeneration.from_pretrained(
            name).to(self.dev).eval()
        self.reader = easyocr.Reader(["en"], gpu=(self.dev == "cuda"))

    def image_to_text(self, path):
        img = cv2.imread(path)
        if img is None:
            raise FileNotFoundError("Could not open image: " + path)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        inp = self.proc(images=rgb, return_tensors="pt").to(self.dev)
        with torch.no_grad():
            out = self.blip.generate(**inp, max_new_tokens=30,
                                     num_beams=3, no_repeat_ngram_size=2)
        cap = self.proc.decode(out[0], skip_special_tokens=True)
        ocr = " ".join(self.reader.readtext(rgb, detail=0))
        return cap, ocr

    def probs(self, items):
        enc = self.tok([t for t, _, _ in items],
                       [f"{a} | {v}" for _, a, v in items],
                       truncation=True, padding=True, max_length=192,
                       return_tensors="pt").to(self.dev)
        with torch.no_grad():
            return torch.softmax(self.model(**enc).logits, -1).float().cpu().numpy()

    def explain(self, text, aspect, cap="", ocr=""):
        chunks = ocr_chunks(aspect, text, ocr)
        toks = text.split()
        vis = build_visual(cap, chunks)
        variants, names = [(text, aspect, vis)], []
        for i, w in enumerate(toks):
            variants.append((" ".join(toks[:i] + toks[i + 1:]), aspect, vis))
            names.append(("word", w))
        if cap:
            variants.append((text, aspect, build_visual("", chunks)))
            names.append(("caption", cap))
        for j, c in enumerate(chunks):
            variants.append((text, aspect, build_visual(cap, chunks[:j] + chunks[j + 1:])))
            names.append(("OCR text", c))

        P = self.probs(variants)
        k = int(P[0].argmax())
        drops = [(names[i][0], names[i][1], float(P[0][k] - P[i + 1][k]))
                 for i in range(len(names))]

        skip = set(aspect.lower().split()) | STOP
        wd = [d for d in drops if d[0] == "word" and d[1].lower() not in skip
              and re.search(r"[A-Za-z0-9]", d[1]) and d[2] > 0.02]
        wd = sorted(wd, key=lambda d: -d[2])[:3]
        vd = [d for d in drops if d[0] != "word"]
        best = max(vd, key=lambda d: abs(d[2])) if vd else None

        s = f"Predicted {LABELS[k].upper()} for '{aspect}' ({P[0][k] * 100:.0f}% confidence). "
        if wd:
            s += "Most influential words: " + ", ".join(f"'{d[1]}'" for d in wd) + ". "
        else:
            s += "No single word dominated the decision. "
        if best and best[2] > 0.03:
            s += f"The image {best[0]} ('{best[1][:60]}') supported this prediction."
        elif best and best[2] < -0.03:
            s += f"The image {best[0]} ('{best[1][:60]}') pushed against this prediction."
        elif vd:
            s += "The image text had little effect."
        return LABELS[k], s

    def run(self, text=None, aspect=None, image_path=None):
        if not text and not image_path:
            print("Please give a text, an image, or both.")
            return
        cap, ocr = "", ""
        if image_path:
            cap, ocr = self.image_to_text(image_path)
        mode = ("text + image" if (text and image_path)
                else "text only" if text else "image only")
        if not text:
            text = cap
        aspect = aspect or "overall"
        label, s = self.explain(text, aspect, cap, ocr)
        print("MODE    :", mode)
        print("TEXT    :", text)
        if image_path:
            print("CAPTION :", cap)
            print("OCR     :", ocr if ocr else "(no text found)")
        print("RESULT  :", label.upper())
        print("EXPLAIN :", s)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="MABSA demo")
    ap.add_argument("--text", help="tweet or review text")
    ap.add_argument("--aspect", help="target aspect, e.g. camera")
    ap.add_argument("--image", help="path to an image")
    ap.add_argument("--model_dir", default="mabsa_model",
                    help="folder with the trained model")
    a = ap.parse_args()
    MABSA(a.model_dir).run(a.text, a.aspect, a.image)
