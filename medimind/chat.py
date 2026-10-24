from .model import predict
from .retrieval import retrieve
NOTICE="Educational information only. MediMind does not diagnose conditions or prescribe treatment. Do not delay professional or emergency care."
ANS={
"sleep":"A consistent sleep schedule and a relaxing wind-down routine may help. Needs vary; seek professional advice if sleep problems persist.",
"nutrition":"A balanced eating pattern generally includes a variety of foods. Individual needs differ; a qualified clinician or dietitian can provide tailored advice.",
"hydration":"Fluid needs vary with activity, climate and health conditions. Follow any fluid guidance provided by your healthcare professional.",
"exercise":"Start gradually with manageable activity. Ask a healthcare professional about safe activity if you have symptoms or a condition affecting exercise.",
"stress":"Regular routines, gentle activity, slow breathing and trusted support may help with everyday stress. Seek professional support if distress persists.",
"blood_pressure":"Blood pressure measures force against artery walls. A chatbot cannot diagnose hypertension; discuss readings with a qualified professional.",
"cold":"The common cold is a viral respiratory illness. Rest and fluids may help comfort. Seek advice for severe, worsening or persistent symptoms.",
"greeting":"Hello! I can explain general health topics and show educational sources. What would you like to learn?",
"help":"Try asking about sleep, nutrition, hydration, exercise, stress, blood pressure or common colds.",
"general_health":"I can share general health education, but cannot assess your personal medical situation or recommend diagnosis or treatment."}
EMERGENCY=["chest pain","difficulty breathing","can't breathe","cannot breathe","not breathing","unconscious","severe bleeding","stroke symptoms","overdose","kill myself","suicidal"]
def answer(message):
    low=message.lower()
    if any(x in low for x in EMERGENCY):
        return {"reply":"This may be an emergency. Contact your local emergency number now (in India, 112) or go to the nearest emergency department. Do not wait for an online chatbot response; follow emergency dispatch instructions.",
        "intent":"emergency","confidence":1.0,"sources":[],"safety_notice":NOTICE,"mode":"emergency_keyword_rule"}
    intent,conf=predict(message); found=retrieve(message)
    if conf<.22:
        intent="uncertain"; reply="I’m not confident I understood. I can explain general topics such as sleep, nutrition, hydration, exercise, stress, blood pressure and common colds. For personal symptoms, consult a qualified healthcare professional."
    else: reply=ANS.get(intent,ANS["general_health"])
    reply += "\\n\\nRelevant educational sources are listed below." if found else "\\n\\nNo relevant source was found in the small demo collection."
    return {"reply":reply,"intent":intent,"confidence":round(conf,3),"sources":found,"safety_notice":NOTICE,"mode":"tfidf_intent_plus_keyword_retrieval"}
