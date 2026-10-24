from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from medimind.model import data,normalize
df=data().dropna(subset=["text","intent"]); X=df.text.astype(str).map(normalize); y=df.intent.astype(str)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
p=Pipeline([("tfidf",TfidfVectorizer()),("clf",LogisticRegression(max_iter=1500,class_weight="balanced"))])
g=GridSearchCV(p,{"tfidf__ngram_range":[(1,1),(1,2)],"clf__C":[.5,1,2]},cv=2,scoring="f1_macro")
g.fit(Xtr,ytr); print("Best params:",g.best_params_); print(classification_report(yte,g.predict(Xte),zero_division=0))
print("Demo dataset only; scores are unstable.")
