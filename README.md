# AI KYC Verification System

## Overview

AI KYC Verification System is a Machine Learning and Computer Vision based project designed to automate Know Your Customer (KYC) verification processes.

The system extracts information from identity documents using OCR, validates the extracted data, and is designed to support advanced verification features such as face matching, fraud detection, and multi-document verification.

Currently, the project supports PAN Card verification using Tesseract OCR and is being expanded to support Aadhaar Cards and additional identity documents.

---

## Features

### Current Features

* PAN Card OCR using Tesseract
* Automatic extraction of:

  * PAN Number
  * Full Name
  * Date of Birth
* PAN Number format validation
* Image preprocessing using OpenCV
* Structured JSON output

### Upcoming Features

* Aadhaar Card OCR
* Face Verification (Selfie vs Document Photo)
* Multi-Document Verification
* Cross-Document Data Matching
* Fraud Detection
* Document Classification
* KYC Risk Scoring
* FastAPI Backend Integration
* Database Storage

---

## Technology Stack

### Programming Language

* Python

### Computer Vision

* OpenCV

### OCR Engine

* Tesseract OCR

### Machine Learning

* Scikit-learn
* TensorFlow (Planned)

### Backend

* FastAPI (Planned)

### Database

* PostgreSQL (Planned)

---

## Project Workflow

1. User uploads a PAN Card image.
2. Image is preprocessed using OpenCV.
3. Tesseract OCR extracts text from the document.
4. Required fields are identified and extracted.
5. PAN Number is validated.
6. Verification results are generated.

Future workflow:

Document Upload
→ OCR Extraction
→ Face Verification
→ Data Validation
→ Fraud Detection
→ KYC Approval/Rejection

---

## Project Structure

```text
AI_KYC_Verification_System/

├── data/
│   ├── input_images/
│   └── output/
│
├── models/
│
├── ocr/
│   ├── pan_ocr.py
│   └── aadhaar_ocr.py
│
├── verification/
│   ├── pan_validation.py
│   ├── aadhaar_validation.py
│   └── face_verification.py
│
├── utils/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Kamlesh-Kumar-ai/AI_KYC_Verification_System.git

cd AI_KYC_Verification_System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Tesseract Installation

Download and install Tesseract OCR.

After installation, configure the executable path:

```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"path_to_tesseract_executable"
```

---

## Future Roadmap

### Phase 1

* PAN OCR Verification ✅

### Phase 2

* Aadhaar OCR Support

### Phase 3

* Face Verification

### Phase 4

* Multi-Document Verification

### Phase 5

* Fraud Detection

### Phase 6

* Complete KYC Automation Platform

---

## Learning Objectives

This project was built to gain hands-on experience in:

* Optical Character Recognition (OCR)
* Computer Vision
* Machine Learning
* Identity Verification Systems
* Fraud Detection
* FastAPI Development
* AI-based KYC Automation

---

## Author

Kamlesh Kumar

Python Developer | Machine Learning Engineer | AI Enthusiast

GitHub:
https://github.com/Kamlesh-Kumar-ai
