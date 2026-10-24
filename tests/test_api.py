from fastapi.testclient import TestClient
from main import app

def test_health():
 with TestClient(app) as c: assert c.get("/api/health").json()["status"]=="ok"
def test_empty_message_rejected():
 with TestClient(app) as c: assert c.post("/api/chat",json={"message":""}).status_code==422
def test_emergency_routing():
 with TestClient(app) as c:
  r=c.post("/api/chat",json={"message":"I have severe chest pain"})
  assert r.status_code==200 and r.json()["intent"]=="emergency"
