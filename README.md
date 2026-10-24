# MediMind AI — Clinical Research Interface Upgrade

## Run in Windows PowerShell (one command per line)
```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000. API docs: http://127.0.0.1:8000/docs.
If Python is not recognized, install Python for Windows, select **Add Python to PATH**, restart VS Code, then retry.

## Evaluate and test (second terminal)
```powershell
.\.venv\Scripts\Activate.ps1
python -m scripts.evaluate_model
python -m pytest -q
python -m scripts.tune_model
```
Refresh the analytics page after evaluation to see actual saved metrics.

## Implemented
- Clinical research dashboard UI with assistant, dataset analytics and source-library views.
- Responsive frontend and FastAPI REST endpoints.
- TF-IDF + Logistic Regression intent classifier.
- Keyword-overlap source retrieval over a small starter collection.
- SQLite development logs and API analytics.
- Held-out evaluation and optional GridSearchCV scripts.

## Not implemented / planned
- No LLM is connected; no generated LLM answers.
- No semantic/vector retrieval; source matching uses keyword overlap.
- No CNN/RNN/LSTM, transfer learning, production MLOps, deployment pipeline or clinical validation.
- Demo dataset is tiny; performance metrics are unstable and do not measure medical correctness.

## Safety and privacy
Educational student prototype only. It cannot diagnose or prescribe. Emergency phrase routing is incomplete and unvalidated. Chat text is stored in local SQLite; do not enter personal or sensitive health information. Verify source pages before academic citation or use.
