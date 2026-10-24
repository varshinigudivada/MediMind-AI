SOURCES=[
{"title":"Healthy diet","publisher":"World Health Organization (WHO)","url":"https://www.who.int/news-room/fact-sheets/detail/healthy-diet","excerpt":"A healthy diet includes a variety of foods; needs vary by person and circumstance.","keywords":["diet","nutrition","food","eat","vegetable","fruit","balanced"]},
{"title":"Physical activity","publisher":"World Health Organization (WHO)","url":"https://www.who.int/news-room/fact-sheets/detail/physical-activity","excerpt":"Regular physical activity can benefit physical and mental health.","keywords":["exercise","activity","walking","fitness","movement"]},
{"title":"Hypertension","publisher":"World Health Organization (WHO)","url":"https://www.who.int/news-room/fact-sheets/detail/hypertension","excerpt":"Hypertension is high blood pressure; clinical decisions should involve qualified professionals.","keywords":["blood pressure","hypertension","pressure","heart"]},
{"title":"Common cold","publisher":"U.S. Centers for Disease Control and Prevention (CDC)","url":"https://www.cdc.gov/common-cold/about/index.html","excerpt":"The common cold is caused by respiratory viruses and can cause a runny nose or sore throat.","keywords":["cold","cough","runny nose","sore throat","virus"]},
{"title":"Sleep and health","publisher":"U.S. Centers for Disease Control and Prevention (CDC)","url":"https://www.cdc.gov/sleep/about/index.html","excerpt":"Healthy sleep supports overall health; sleep needs vary.","keywords":["sleep","insomnia","rest","tired","bedtime"]},
{"title":"Mental health self-care","publisher":"National Institute of Mental Health (NIMH)","url":"https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health","excerpt":"Healthy routines, social support and professional help can support mental health.","keywords":["stress","overwhelmed","anxiety","mental health","worry"]},
{"title":"Water and healthier choices","publisher":"U.S. Centers for Disease Control and Prevention (CDC)","url":"https://www.cdc.gov/healthy-water-data/about/index.html","excerpt":"Water is important for health; fluid needs vary with activity, climate and health conditions.","keywords":["water","hydration","drink","fluids","dehydration"]}]
def retrieve(query,limit=2):
    q=query.lower(); scored=[]
    for s in SOURCES:
        score=sum(1 for k in s["keywords"] if k in q)
        if score: scored.append((score,s))
    scored.sort(key=lambda x:x[0],reverse=True)
    return [{k:v for k,v in s.items() if k!="keywords"} for _,s in scored[:limit]]
def sources(): return [{k:v for k,v in s.items() if k!="keywords"} for s in SOURCES]
