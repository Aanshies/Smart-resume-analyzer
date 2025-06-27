📝 Smart Resume Analyzer: AI-Powered Resume Screening with NLP & Streamlit
Smart Resume Analyzer is an 🤖 AI-powered resume matcher and analyzer using NLP and Streamlit, designed to automate resume screening for recruiters by comparing resumes with job descriptions and calculating match percentages for efficient shortlisting.

📑 Table of Contents
🚀 Project Overview

✨ Features

⚙️ Installation

📂 Dataset

🖥️ Usage

📄 Uploading Resumes

✅ Viewing Match Scores

🧠 Model Details

🪄 Text Preprocessing

📊 Similarity Calculation

🌐 Streamlit Deployment

🤝 Contributing

🛡️ License

🏷️ Tags

🚀 Project Overview
Smart Resume Analyzer automates initial resume screening using natural language processing (NLP) to compute similarity between job descriptions and candidate resumes. It reduces manual screening workload and helps in quick, data-driven candidate shortlisting for recruiters.

✨ Features
✅ Upload Multiple Resumes (PDF)
✅ Input/Paste Job Description
✅ Automated Similarity Matching using cosine similarity on TF-IDF vectors
✅ Visual Match Scores on a clean Streamlit interface
✅ Download Shortlist for further review

⚙️ Installation
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/Aanshies/Smart-resume-analyzer.git
2️⃣ Install Dependencies
bash
Copy code
cd Smart-resume-analyzer
pip install -r requirements.txt
📂 Dataset
This project does not require a dataset as it uses real-time processing on uploaded resumes and provided job descriptions.

🖥️ Usage
📄 Uploading Resumes
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Upload one or multiple PDF resumes.

Paste or upload the job description.

Click Analyze to compute match percentages.

✅ Viewing Match Scores
View each candidate’s match percentage.

Sort candidates based on scores for easy shortlisting.

Export shortlisted candidates for review.

🧠 Model Details
🪄 Text Preprocessing
Text extraction from PDFs (PyPDF2).

Lowercasing and special character removal.

Tokenization and stopword removal.

TF-IDF vectorization to convert text into numerical representations.

📊 Similarity Calculation
Calculates cosine similarity between job descriptions and resumes to determine fit scores.

🌐 Streamlit Deployment
Deploy on Streamlit Community Cloud or your server for accessible online resume screening.

🌐 Hosted Demo <!-- Replace with your actual Streamlit app URL -->

🤝 Contributing
Contributions are welcome! 🚀

1️⃣ Fork the repository
2️⃣ Create a feature branch
3️⃣ Commit with clear messages
4️⃣ Push and create a pull request

🛡️ License
Licensed under the MIT License. See LICENSE for details.
