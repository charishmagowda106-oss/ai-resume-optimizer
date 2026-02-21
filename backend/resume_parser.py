from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF

SKILL_SET = [
    "perl",
    "java",
    "c++",
    "html",
    "php",
    "mysql",
    "matlab",
    "machine learning",
    "artificial intelligence",
    "linux",
    "windows",
    "mac os"
]

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILL_SET:
        if skill in text:
            found_skills.append(skill)

    return found_skills

def calculate_match(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(similarity_score[0][0] * 100, 2)