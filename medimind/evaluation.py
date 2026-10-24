import json
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from .model import data,normalize
from .config import DATA_DIR

def evaluate():
    df=data().dropna(subset=["text","intent"]).copy(); df["text"]=df.text.astype(str).map(normalize)
    counts=df.intent.value_counts()
    if len(df)<12 or (counts<2).any(): raise ValueError("Need at least two examples per intent for stratified evaluation.")
    Xtr,Xte,ytr,yte=train_test_split(df.text,df.intent,test_size=.25,random_state=42,stratify=df.intent)
    pipe=Pipeline([("tfidf",TfidfVectorizer(ngram_range=(1,2),sublinear_tf=True)),("clf",LogisticRegression(max_iter=1200,class_weight="balanced",random_state=42))])
    pipe.fit(Xtr,ytr); pred=pipe.predict(Xte); report=classification_report(yte,pred,output_dict=True,zero_division=0)
    out={"dataset_rows":len(df),"train_rows":len(Xtr),"test_rows":len(Xte),"accuracy":float(accuracy_score(yte,pred)),
    "macro_f1":report["macro avg"]["f1-score"],"weighted_f1":report["weighted avg"]["f1-score"],
    "classification_report":report,"labels":sorted(df.intent.unique()),"confusion_matrix":confusion_matrix(yte,pred,labels=sorted(df.intent.unique())).tolist(),
    "warning":"Tiny demo dataset only; metrics are unstable and do not indicate medical correctness."}
    DATA_DIR.mkdir(exist_ok=True); (DATA_DIR/"evaluation_results.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
    return out
def summary():
    p=DATA_DIR/"evaluation_results.json"
    return json.loads(p.read_text()) if p.exists() else {"status":"not_run","message":"Run python -m scripts.evaluate_model"}
