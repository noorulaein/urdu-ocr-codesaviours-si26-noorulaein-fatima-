# Urdu OCR using TrOCR
### A Fine-Tuned TrOCR Model for Extracting Printed Urdu Text from Images

## Project Overview

This project is an Optical Character Recognition (OCR) system developed for extracting printed Urdu text from images using Microsoft's TrOCR (Transformer-based OCR) model. The model was fine-tuned on a custom Urdu image dataset during the Code Saviours ML/AI Internship (Batch SI-26).

The project is deployed as a live web application using **Gradio** and **Hugging Face Spaces**, allowing users to upload Urdu text images and receive extracted text through a simple interface.

---

# Problem Statement

Optical Character Recognition for Urdu is significantly more challenging than English because Urdu uses the Nastaliq writing style. Nastaliq contains:

- Complex ligatures
- Connected characters
- Variable character shapes
- Overlapping words
- Right-to-left writing direction

These characteristics make Urdu OCR a difficult computer vision problem.

A reliable Urdu OCR system can help digitize books, newspapers, historical archives, educational material, and official documents.

---

# How the Project Works

The project uses Microsoft's **TrOCR (Transformer-based Optical Character Recognition)** model.

### Workflow

1. User uploads an Urdu image.
2. The image is preprocessed using the TrOCR Processor.
3. The fine-tuned VisionEncoderDecoder model predicts the text.
4. The generated tokens are decoded into readable Urdu text.
5. The extracted text is displayed in the Gradio interface.

The model was fine-tuned on a custom dataset consisting of printed Urdu text images and corresponding labels.

---

# Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- TrOCR
- Gradio
- Google Colab
- Hugging Face Spaces
- Pillow

---

# Live Demo

**Hugging Face Space**

(https://huggingface.co/spaces/noorulaeinfatima/urdu-ocr-codesaviours-si26-noorulaeinfatima)

---

# How to Run Locally

Clone the repository

```bash
git clone(https://github.com/noorulaein/urdu-ocr-codesaviours-si26-noorulaein-fatima)
```

Move into the project directory

```bash
cd YOUR_REPOSITORY
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

The Gradio application will open in your browser.

---

# Dataset

The model was fine-tuned using a custom Urdu OCR dataset created during the internship.

Dataset characteristics include:

- Printed Urdu text images
- Multiple image sizes
- Different fonts
- Various word lengths
- Image preprocessing before training

The dataset was collected and prepared using publicly available Urdu text sources and custom-generated samples.

---

# Model Results

### Training Summary

- Base Model: Microsoft TrOCR (Printed)
- Framework: Hugging Face Transformers
- Fine-tuned using PyTorch
- Deployment: Hugging Face Spaces

### Accuracy

Current Model Accuracy:

**Approximately 2%**

### Current Limitations

The current model does not accurately extract Urdu text because of several factors:

- The training dataset is relatively small.
- Urdu Nastaliq script is highly complex.
- The model was trained for a limited number of epochs.
- The dataset does not contain enough font and layout diversity.
- Additional preprocessing techniques could further improve recognition quality.

Because of these limitations, the application may generate incomplete text or unreadable characters for many images.

---

# Future Improvements

The model can be significantly improved by:

- Increasing the dataset size to several thousand images.
- Collecting images from books, newspapers, and signboards.
- Including more Urdu fonts and writing styles.
- Applying stronger preprocessing techniques.
- Training for more epochs.
- Performing hyperparameter tuning.
- Using a larger TrOCR checkpoint or experimenting with other OCR architectures.

These improvements are expected to substantially increase OCR accuracy and make the application more suitable for real-world use.

---

# Screenshots

## Gradio Interface

<img width="793" height="317" alt="image" src="https://github.com/user-attachments/assets/c2f33267-8c76-4408-9678-38dfceaaabf4" />


## Prediction Example

<img width="786" height="510" alt="image" src="https://github.com/user-attachments/assets/97b39c27-6a22-4881-8ba3-8070883d3569" />


---

# Project Structure

```
project/
│
├── app.py
├── requirements.txt
├── config.json
├── model.safetensors
├── tokenizer files
├── README.md
└── images/
```
## Note

The trained model weights are not included in this repository because the fine-tuned TrOCR model exceeds GitHub's file size limit. The application was developed and tested locally using the trained model.
---

# Author

**Noorulaein Fatima**

Built during the **Code Saviours ML/AI Internship — Batch SI-26**

---
