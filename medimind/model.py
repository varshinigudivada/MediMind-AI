import re, unicodedata
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from .config import CSV_PATH

DEMO=[("How can I improve my sleep?","sleep"),("Tips for sleeping better","sleep"),("Why is good sleep important?","sleep"),
("How do I eat a balanced diet?","nutrition"),("What are healthy food choices?","nutrition"),("Explain healthy eating","nutrition"),
("How much water should I drink?","hydration"),("Why is water important?","hydration"),
("How can I start exercising safely?","exercise"),("Benefits of physical activity","exercise"),
("How can I manage everyday stress?","stress"),("I feel stressed and overwhelmed","stress"),
("What is blood pressure?","blood_pressure"),("Explain high blood pressure","blood_pressure"),
("What is a common cold?","cold"),("Why do people get a runny nose?","cold"),
("Hello","greeting"),("Hi there","greeting"),("What can you do?","help"),("Help me use this chatbot","help"),
("How do vaccines work?","general_health"),("What is a healthy lifestyle?","general_health"),
("What is first aid?","general_health"),("How can I stay healthy?","general_health")]
def normalize(s):
    s=unicodedata.normalize("NFKC", str(s or "")).lower().strip()
    s=re.sub(r"https?://\S+", " ", s)
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s'-]", " ", s)).strip()
def data():
    if CSV_PATH.exists():
        df=pd.read_csv(CSV_PATH)
        if {"text","intent"}.issubset(df.columns) and len(df)>=12:
            return df.dropna(subset=["text","intent"])
    return pd.DataFrame(DEMO,columns=["text","intent"])
def build():
    df=data()
    return Pipeline([("tfidf",TfidfVectorizer(ngram_range=(1,2),sublinear_tf=True)),
        ("clf",LogisticRegression(max_iter=1200,class_weight="balanced",random_state=42))]).fit(df.text.map(normalize),df.intent)
MODEL=build()
def predict(text):
    p=MODEL.predict_proba([normalize(text)])[0]; i=int(p.argmax())
    return str(MODEL.classes_[i]),float(p[i])
