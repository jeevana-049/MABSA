# MABSA

## An Explainable Multimodal Framework for Aspect-Based Sentiment Analysis using Image-to-Text Conversion and Aspect-Oriented Filtration

MABSA is an Explainable Multimodal Aspect-Based Sentiment Analysis framework designed to analyze customer opinions expressed through both **text and images**.

Traditional sentiment analysis systems mainly focus on textual information and may miss important visual cues present in customer feedback. MABSA addresses this limitation by combining textual and visual information through **Image-to-Text Conversion, OCR, Image Captioning, Aspect-Oriented Filtration, and Aspect-Level Sentiment Classification**.

The framework aims to provide more accurate, transparent, and explainable sentiment analysis for multimodal customer feedback.

---

## 📌 Project Overview

Customers increasingly express their opinions using a combination of textual reviews and images. A review may contain positive sentiment toward one aspect and negative sentiment toward another.

For example:

> "Great camera, but the delivery was slow."

MABSA can identify the different aspects and associate sentiment with each aspect:

| Aspect | Sentiment |
|---|---|
| Camera | Positive |
| Delivery | Negative |

By combining textual and visual information, MABSA provides a more comprehensive understanding of customer feedback.

---

## 🎯 Problem Statement

Customers express opinions through both text and images, but traditional sentiment analysis mainly focuses on text and may miss important visual information.

This can lead to incomplete sentiment understanding and inaccurate aspect-level analysis.

Therefore, an explainable multimodal framework is needed to combine textual and visual information for more accurate customer-feedback analysis.

---

## 🎯 Objectives

- Develop an Explainable Multimodal Aspect-Based Sentiment Analysis framework.
- Analyze customer opinions using both text and images.
- Extract visual information using Image-to-Text Conversion, OCR, and Image Captioning.
- Perform aspect-level sentiment classification.
- Classify sentiment into Positive, Neutral, and Negative categories.
- Improve accuracy, transparency, and reliability through Explainable AI.
- Provide meaningful aspect-level insights from multimodal customer feedback.

---

## ✨ Key Features

### Multimodal Sentiment Analysis

Processes both textual reviews and images to obtain a more comprehensive understanding of customer opinions.

### Image-to-Text Conversion

Extracts useful information from images using techniques such as:

- OCR
- Image Captioning
- Image-to-Text Conversion

### Aspect-Oriented Filtration

Identifies and filters relevant aspects from the combined textual and visual information.

### Aspect-Level Sentiment Classification

Determines the sentiment associated with individual aspects:

- Positive
- Neutral
- Negative

### Explainable Results

Provides interpretable sentiment results by connecting identified aspects with their corresponding sentiment.

---

## 🏗️ Proposed Methodology

The MABSA framework follows the pipeline below:

```text
        Textual Reviews + Images
                  |
                  v
       Image-to-Text Conversion
          OCR + Image Captioning
                  |
                  v
       Text + Visual Information
                  |
                  v
     Aspect-Oriented Preprocessing
             / Filtration
                  |
                  v
      Aspect-Level Sentiment
           Classification
                  |
        +---------+---------+
        |         |         |
        v         v         v
     Positive   Neutral   Negative
                  |
                  v
        Explainable Result

---

## 🛠️ Technologies

Python, PyTorch, Hugging Face Transformers (BLIP, RoBERTa), EasyOCR, Pandas, NumPy

## 📊 Dataset

MVSA-Multiple (image-text pairs with sentiment labels)

## 🚀 Current Status

- [x] Image captioning (BLIP)
- [x] OCR (EasyOCR)
- [x] Three modes: text only, image only, text + image
- [x] Basic aspect filtration and sentiment prediction
- [ ] MVSA-Multiple dataset loading
- [ ] Model fine-tuning
- [ ] Explainability (SHAP / LIME)
- [ ] Demo UI (Streamlit / Gradio)

## 👥 Team (Batch 6)

| Name | Roll No. |
|---|---|
| G. Jeevana | 23AG1A05E8 |
| G. Sivakumar Reddy | 23AG1A05F1 |
| B. Saikumar | 23AG1A05D6 |

**Guide:** Dr. P Chiranjeevi
**Institution:** ACE Engineering College, Dept. of CSE
