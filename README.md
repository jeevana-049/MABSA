# MABSA

## An Explainable Multimodal Framework for Aspect-Based Sentiment Analysis using Image-to-Text Conversion and Aspect-Oriented Filtration

**ACE Engineering College (Autonomous) | Department of Computer Science and Engineering | Major Project Stage - I**

MABSA is an Explainable Multimodal Aspect-Based Sentiment Analysis framework designed to analyze customer opinions expressed through both **text and images**.

Traditional sentiment analysis systems mainly focus on textual information and may miss important visual cues present in customer feedback. MABSA addresses this limitation by combining textual and visual information through **Image-to-Text Conversion, OCR, Image Captioning, Aspect-Oriented Filtration, and Aspect-Level Sentiment Classification**.

The framework aims to provide more accurate, transparent, and explainable sentiment analysis for multimodal customer feedback.

---

## Project Overview

Customers increasingly express their opinions using a combination of textual reviews and images. A single review may contain positive sentiment toward one aspect and negative sentiment toward another.

For example:

> "Great camera, but the delivery was slow."

MABSA identifies the different aspects and associates a sentiment with each one:

| Aspect | Sentiment |
|---|---|
| Camera | Positive |
| Delivery | Negative |

By combining textual and visual information, MABSA provides a more complete understanding of customer feedback.

---

## Problem Statement

Customers express opinions through both text and images, but traditional sentiment analysis mainly focuses on text and may miss important visual information.

This can lead to incomplete sentiment understanding and inaccurate aspect-level analysis.

Therefore, an explainable multimodal framework is needed to combine textual and visual information for more accurate customer-feedback analysis.

---

## Objectives

- Develop an Explainable Multimodal Aspect-Based Sentiment Analysis framework.
- Analyze customer opinions using both text and images.
- Extract visual information using Image-to-Text Conversion, OCR, and Image Captioning.
- Perform aspect-level sentiment classification.
- Classify sentiment into Positive, Neutral, and Negative categories.
- Improve accuracy, transparency, and reliability through Explainable AI.
- Provide meaningful aspect-level insights from multimodal customer feedback.

---

## Key Features

### Multimodal Sentiment Analysis
Processes textual reviews, images, or both together to obtain a more complete understanding of customer opinions.

### Image-to-Text Conversion
Extracts useful information from images using:
- **Image Captioning** (BLIP) to describe the scene or product
- **OCR** (EasyOCR) to read any text written inside the image

### Aspect-Oriented Filtration
Keeps only the information relevant to the target aspect and reduces the influence of irrelevant content.

### Aspect-Level Sentiment Classification
Determines the sentiment associated with each aspect:
- Positive
- Neutral
- Negative

### Explainable Results
Provides interpretable results by connecting each aspect with its predicted sentiment and the evidence behind it.

---

## Supported Input Modes

| Mode | Input | Description |
|---|---|---|
| Text only | Review text | Sentiment is predicted from the text |
| Image only | Photo | Caption and OCR convert the image to text, then sentiment is predicted |
| Text + Image | Review and photo | Text, caption, and OCR are combined, then sentiment is predicted |

---

## Proposed Methodology

```mermaid
flowchart TD
    A[Textual Reviews + Images] --> B[Image-to-Text Conversion<br/>OCR + Image Captioning]
    B --> C[Text + Visual Information]
    C --> D[Aspect-Oriented Preprocessing / Filtration]
    D --> E[Aspect-Level Sentiment Classification]
    E --> F[Positive]
    E --> G[Neutral]
    E --> H[Negative]
    F --> I[Explainable Result]
    G --> I
    H --> I
```

**Steps**
1. Take a review (text), an image, or both as input.
2. Convert the image to text using BLIP captioning and EasyOCR.
3. Combine the review text with the visual information.
4. Filter the combined content by the target aspect.
5. Classify the aspect-level sentiment.
6. Generate an explainable result.

---

## Technologies and Tools

| Category | Tools |
|---|---|
| Language | Python |
| Deep Learning | PyTorch, Hugging Face Transformers |
| Image-to-Text | BLIP (captioning), EasyOCR (OCR) |
| Sentiment Model | RoBERTa-based classifier |
| Data Handling | Pandas, NumPy, OpenCV, Pillow |
| Development | Google Colab, VS Code, Git and GitHub |

---

## Dataset

**MVSA-Multiple**: a multimodal dataset of image-text pairs with sentiment labels (Positive, Neutral, Negative).

---

## Getting Started

### Run on Google Colab
1. Open the notebook from this repository in Google Colab.
2. Go to **Runtime > Change runtime type** and select **T4 GPU**.
3. Run the cells from top to bottom.

### Install dependencies
```bash
pip install transformers torch pillow requests easyocr
```

### Quick example
```python
# Text only
analyze(text="Great camera, but the delivery was slow.", aspect="camera")

# Image only
analyze(image_path="sample.png")

# Text + image
analyze(text="The battery is terrible.", image_path="sample.png", aspect="battery")
```

---

## Current Status

- [x] Image captioning (BLIP)
- [x] OCR (EasyOCR)
- [x] Three modes: text only, image only, text + image
- [x] Basic aspect filtration and sentiment prediction
- [ ] MVSA-Multiple dataset loading and cleaning
- [ ] Captioning and OCR on the full dataset
- [ ] Aspect-oriented attention-based filtration
- [ ] Model fine-tuning and evaluation (Accuracy, Macro-F1)
- [ ] Explainability (SHAP / LIME and natural-language explanations)
- [ ] Demo UI (Streamlit / Gradio)

---

## Expected Outcomes

- Comprehensive sentiment understanding using text and images
- Positive, Neutral, and Negative aspect classification
- Explainable sentiment predictions
- Improved transparency in customer-feedback analysis

---

## Impact and Practical Applicability

**Real-world impact:** Provides a deeper understanding of customer opinions by combining textual and visual information with aspect-level explainable sentiment analysis.

**Practical implementation:** Can be integrated into e-commerce, product-review, and social-media feedback systems to analyze multimodal customer opinions.

**Beneficiaries:** Businesses, product teams, marketing teams, customer support teams, researchers, and analysts.

---

## Sustainable Development Goal

**SDG 9: Industry, Innovation and Infrastructure**
Supports AI-driven innovation by enabling intelligent multimodal analysis for digital customer feedback.

---

## Team (Batch 6)

| Name | Roll No. |
|---|---|
| G. Jeevana | 23AG1A05E8 |
| G. Sivakumar Reddy | 23AG1A05F1 |
| B. Saikumar | 23AG1A05D6 |

## Faculty

| Role | Name |
|---|---|
| Project Guide | Dr. P Chiranjeevi, Professor |
| Project Coordinator | Dr. S Raghu, Associate Professor |
| HOS-CSE-C | Mr. V Chandra Sekhar Reddy, Associate Professor |
| HOD, CSE Dept | Dr. Ch. Vijaya Kumar, Professor |

---

## Repository

[github.com/jeevana-049/MABSA](https://github.com/jeevana-049/MABSA)
