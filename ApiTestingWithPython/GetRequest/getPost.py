from http.client import responses

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
load_dotenv()

def test_get_products():
    with sync_playwright() as p:
        api_request=p.request.new_context(base_url=os.getenv("BASEURL_GETREQUEST"))
        response=api_request.get("/products/2")

        data=response.json()
        assert response.status==200
        assert data["id"]==2
