#!/usr/bin/env bash

# Install dependencies first
pip install -r requirements.txt

# Then download the spacy model
python -m spacy download en_core_web_sm
