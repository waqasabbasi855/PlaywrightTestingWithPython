import os

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()


def test_delete_user():
    with sync_playwright() as p:
        api_request_context=p.request.new_context(base_url=os.getenv("BASEURL_DELETEREQUEST"))
        response=api_request_context.delete("posts/100")
        assert response.status==200