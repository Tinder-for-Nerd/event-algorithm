from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)
resp = client.post('/score_skill', json={
  'name':'React', 'domain':'Frontend', 'months_since_use':1, 'role_months':12, 'seniority_level':'built', 'endorsement_count':5, 'self_reported_level':'advanced'
})
print('status', resp.status_code)
print(resp.json())
