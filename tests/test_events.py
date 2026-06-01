import json
import unittest

from fastapi.testclient import TestClient

from api.app import app


class EventSearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_search_events_prefers_matching_skills(self):
        payload = {
            "skills": [
                {"name": "Python", "domain": "Backend", "months_since_use": 1, "role_months": 24},
                {"name": "Pandas", "domain": "Data", "months_since_use": 2, "role_months": 18},
            ],
            "events": [
                {
                    "id": "e1",
                    "title": "Intro to Python for Data",
                    "required_skills": {"Python": 0.9, "Pandas": 0.6},
                    "start_time": "2026-06-15T09:00:00+00:00",
                    "popularity": 0.7,
                },
                {
                    "id": "e2",
                    "title": "Advanced System Design",
                    "required_skills": {"System Design": 0.9, "Distributed Systems": 0.8},
                    "start_time": "2026-07-20T09:00:00+00:00",
                    "popularity": 0.6,
                },
            ],
            "top_k": 2,
        }

        resp = self.client.post("/search_events", json=payload)
        self.assertEqual(resp.status_code, 200)
        body = resp.json()
        self.assertIn("results", body)
        results = body["results"]
        self.assertGreaterEqual(len(results), 1)
        # Top result should be the Python event
        self.assertEqual(results[0]["event_id"], "e1")


if __name__ == "__main__":
    unittest.main()
