from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
import json
import re

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "data" / "faqs.json"


def load_faqs():
    with open(FAQ_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


faq_data = load_faqs()

faq_questions = [item["question"] for item in faq_data]
cleaned_questions = [clean_text(question) for question in faq_questions]

vectorizer = TfidfVectorizer(stop_words="english")
faq_vectors = vectorizer.fit_transform(cleaned_questions)


def get_best_answer(user_question):
    cleaned_user_question = clean_text(user_question)

    if not cleaned_user_question:
        return {
            "answer": "Please type a question so I can help you.",
            "matched_question": "",
            "confidence": 0
        }

    user_vector = vectorizer.transform([cleaned_user_question])
    similarity_scores = cosine_similarity(user_vector, faq_vectors)

    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_match_index]

    confidence_percentage = round(float(best_score) * 100, 2)

    if best_score < 0.20:
        return {
            "answer": "Sorry, I could not find a suitable answer for your question. Please try asking something related to AI, machine learning, NLP, Flask, or this chatbot project.",
            "matched_question": "No close match found",
            "confidence": confidence_percentage
        }

    return {
        "answer": faq_data[best_match_index]["answer"],
        "matched_question": faq_data[best_match_index]["question"],
        "confidence": confidence_percentage
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_question = data.get("question", "")

    result = get_best_answer(user_question)

    return jsonify({
        "answer": result["answer"],
        "matched_question": result["matched_question"],
        "confidence": result["confidence"]
    })


if __name__ == "__main__":
    app.run(debug=True)