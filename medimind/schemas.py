from pydantic import BaseModel, Field
from typing import List

class ChatRequest(BaseModel):
    message:str=Field(min_length=1,max_length=1200)

class Source(BaseModel):
    title:str
    publisher:str
    url:str
    excerpt:str

class ChatResponse(BaseModel):
    reply:str
    intent:str
    confidence:float
    sources:List[Source]=[]
    safety_notice:str
    mode:str
