from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
load_dotenv()

def test_create_user():
    with sync_playwright() as p:
        api_request_context = p.request.new_context(base_url=os.getenv("BASEURL_POSTREQUEST"))
        payload = {
            "userId": 1,
            "id": 1,
            "title": "are or make repel provide blinded except option reprehend",
            "body": "because and undertakes\ntakes upon the objections that follow expeditiously and when\nreprehends the annoyances as which all\nour things are but are things happen to the architect"
            }

        response = api_request_context.post("posts", data=payload)
        assert response.status == 201
        new_user = response.json()
        assert new_user["title"] == "are or make repel provide blinded except option reprehend"
