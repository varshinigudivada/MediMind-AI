from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from medimind.config import STATIC_DIR
from medimind.db import init_db, save_chat, log_summary
from medimind.chat import answer
from medimind.retrieval import sources
from medimind.evaluation import summary
from medimind.model import data
from medimind.schemas import ChatRequest, ChatResponse

@asynccontextmanager
async def lifespan(app):
    init_db()
    yield

app = FastAPI(title="MediMind AI Research Prototype", version="3.0.0",
              description="Educational health-information chatbot; not a diagnostic tool.")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return (STATIC_DIR / "index.html").read_text(encoding="utf-8")

@app.get("/api/health")
def health():
    return {"status":"ok", "classifier":"TF-IDF + Logistic Regression",
            "retrieval":"keyword-overlap baseline", "llm":"not connected",
            "medical_validation":"not performed"}

@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    message = req.message.strip()
    result = answer(message)
    save_chat(message, result["intent"], result["confidence"])
    return ChatResponse(**result)

@app.get("/api/sources")
def source_list():
    return {"sources": sources()}

@app.get("/api/metrics")
def metrics():
    return summary()

@app.get("/api/analytics")
def analytics():
    df = data().dropna(subset=["text", "intent"])
    counts = df["intent"].value_counts().sort_index()
    return {"dataset_rows": int(len(df)), "intent_count": int(df["intent"].nunique()),
            "intents": [{"label": str(k), "count": int(v)} for k, v in counts.items()],
            "source_count": len(sources()), "chat_log": log_summary(),
            "model": "TF-IDF + Logistic Regression",
            "evaluation_note": "Run the evaluation script for held-out metrics. Demo dataset is tiny; metrics are not clinical validation."}
