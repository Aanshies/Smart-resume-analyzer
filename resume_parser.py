# resume_parser.py

import fitz  # PyMuPDF
import spacy
from fuzzywuzzy import fuzz

import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        return ""


def extract_keywords(text):
    """Get important keywords from the text using spaCy"""
    doc = nlp(text)
    return list(set([token.lemma_.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop]
))


def match_keywords(resume_keywords, jd_keywords):
    matched_keywords = []
    match_score = 0

    for r_kw in resume_keywords:
        for jd_kw in jd_keywords:
            if fuzz.partial_ratio(r_kw.lower(), jd_kw.lower()) > 80:
                matched_keywords.append(r_kw)
                break

    if jd_keywords:
        match_percentage = (len(matched_keywords) / len(jd_keywords)) * 100
    else:
        match_percentage = 0

    return match_percentage, matched_keywords
