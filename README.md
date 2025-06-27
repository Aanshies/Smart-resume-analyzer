# 📝 Smart Resume Analyzer: AI-Powered Resume Screening with NLP & Streamlit
![Smart Resume Analyzer Screenshot](https://github.com/user-attachments/assets/c6126feb-5b89-45d1-b996-1d849f6f45b0)

**Smart Resume Analyzer** is an 🤖 AI-powered resume matcher and analyzer using **NLP and Streamlit**, designed to automate resume screening for recruiters by comparing resumes with job descriptions and calculating match percentages for efficient shortlisting.

---

## 📑 Table of Contents

- 🚀 Project Overview
- ✨ Features
- ⚙️ Installation
- 📂 Dataset
- 🖥️ Usage
  - 📄 Uploading Resumes
  - ✅ Viewing Match Scores
- 🧠 Model Details
  - 🪄 Text Preprocessing
  - 📊 Similarity Calculation
- 🌐 Streamlit Deployment
- 🤝 Contributing
- 🛡️ License
- 🏷️ Tags

---

## 🚀 Project Overview

Smart Resume Analyzer automates initial resume screening using **Natural Language Processing (NLP)** to compute similarity between job descriptions and candidate resumes. It reduces manual screening workload and helps in **quick, data-driven candidate shortlisting** for recruiters.

---

## ✨ Features

- ✅ Upload Multiple Resumes (PDF)
- ✅ Input/Paste Job Description
- ✅ Automated Similarity Matching using cosine similarity on TF-IDF vectors
- ✅ Visual Match Scores on a clean Streamlit interface
- ✅ Download shortlist for further review

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Aanshies/Smart-resume-analyzer.git
```

### 2️⃣ Install Dependencies
```bash
cd Smart-resume-analyzer
pip install -r requirements.txt
```

## 📂 Dataset
This project does not require a dataset as it uses real-time processing on uploaded resumes and provided job descriptions.

## 🖥️ Usage
📄 Uploading Resumes
Run the Streamlit app:
```bash
streamlit run app.py
```
- Upload one or multiple PDF resumes.

- Paste or upload the job description.

- Click Analyze to compute match percentages.

## ✅ Viewing Match Scores
- View each candidate’s match percentage.

- Sort candidates based on scores for easy shortlisting.

- Export shortlisted candidates for review.

## 🧠 Model Details
### 🪄 Text Preprocessing
- Extracts text from PDFs using PyPDF2.

- Converts text to lowercase and removes special characters.

- Tokenizes and removes stopwords.

- Uses TF-IDF vectorization to convert text into numerical representations.

### 📊 Similarity Calculation
- Calculates cosine similarity between job descriptions and resumes to determine fit scores.

### 🌐 Streamlit Deployment
- Deploy on Streamlit Community Cloud or your server for accessible online resume screening.

### 🌐 Hosted Demo: [Smart Resume Analyzer
](http://192.168.179.248:8501/#smart-resume-analyzer)

### 🤝 Contributing
- Contributions are welcome! 🚀

- Fork the repository.

- Create a feature branch.

- Commit with clear messages.

- Push and create a pull request.



