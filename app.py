import streamlit as st
from resume_parser import extract_text_from_pdf, extract_keywords, match_keywords

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

import spacy
import os

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Download if not found
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Custom CSS for Beautiful UI
st.markdown("""
    <style>
    body {
        background-color: #f7f9fb;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.05);
        margin: auto;
        width: 90%;
    }
    .stButton > button {
        background-color: #4CAF50 !important;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
    }
    .stProgress > div > div > div {
        background-color: #4CAF50 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main Section
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("## 🤖 Smart Resume Analyzer")
st.markdown("Smartly match your resume with job descriptions using AI, NLP & ATS logic.")

st.markdown("---")

# Resume Upload
st.markdown("### 📄 Upload Your Resume")
resume_file = st.file_uploader("Upload your resume as a PDF", type=["pdf"])

# Job Description Input
st.markdown("### 💼 Enter Job Description")
jd_input_mode = st.radio("How do you want to provide the JD?", ["📄 Upload .txt File", "✍️ Paste JD"])

job_description_text = ""

if jd_input_mode == "📄 Upload .txt File":
    jd_file = st.file_uploader("Upload the job description file", type=["txt"])
    if jd_file:
        job_description_text = jd_file.read().decode("utf-8")
elif jd_input_mode == "✍️ Paste JD":
    job_description_text = st.text_area("Paste the job description here", height=200)

# Analyze Button
if st.button("🚀 Run Analysis"):
    if resume_file and job_description_text.strip() != "":
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(resume_file)
            resume_keywords = extract_keywords(resume_text)
            jd_keywords = extract_keywords(job_description_text)
            ats_score, matched_keywords = match_keywords(resume_keywords, jd_keywords)
            missing_keywords = list(set(jd_keywords) - set(matched_keywords))

        # Results Display
        st.success("✅ Analysis Complete")

        st.markdown("### 📊 ATS Compatibility Score")
        st.progress(int(ats_score))
        st.markdown(f"**Your Resume ATS Score: `{ats_score:.2f}%`**")

        st.markdown("### ✅ Matched Keywords")
        st.info(", ".join(matched_keywords) if matched_keywords else "No matches found.")

        st.markdown("### ⚠️ Missing Keywords (Add these)")
        if missing_keywords:
            st.warning(", ".join(missing_keywords))
        else:
            st.success("Your resume covers all key JD terms!")

        st.markdown("### 💡 Improvement Suggestions")
        st.markdown("""
        - Add missing job-related keywords to improve your score.
        - Use consistent titles and tech stack names.
        - Emphasize tools, frameworks, and results.
        - Keep formatting clean for ATS compatibility.
        """)
    else:
        st.error("Please upload both resume and job description.")

st.markdown("</div>", unsafe_allow_html=True)
