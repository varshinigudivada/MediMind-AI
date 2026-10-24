from medimind.evaluation import evaluate
if __name__=="__main__":
 r=evaluate()
 print("Rows:",r["dataset_rows"],"Train:",r["train_rows"],"Test:",r["test_rows"])
 print("Accuracy:",round(r["accuracy"],3),"Macro-F1:",round(r["macro_f1"],3),"Weighted-F1:",round(r["weighted_f1"],3))
 print(r["warning"])
