# CodeAlpha FAQ Chatbot

A simple FAQ chatbot web application developed as part of the CodeAlpha Artificial Intelligence Internship. This chatbot answers user questions by matching them with the most relevant FAQ from a prepared dataset using TF-IDF and cosine similarity.

## Project Overview

This project demonstrates how Natural Language Processing techniques can be used to build a question-answering chatbot. The chatbot takes a user question, preprocesses the text, compares it with stored FAQ questions and returns the best matching answer.

## Features

- User-friendly chatbot interface
- FAQ dataset stored in JSON format
- Text preprocessing
- TF-IDF vectorization
- Cosine similarity-based question matching
- Confidence score display
- Suggested question buttons
- Responsive web design

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Scikit-learn
- TF-IDF
- Cosine Similarity

## Project Structure

```text
CodeAlpha_FAQ_Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── faqs.json
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
