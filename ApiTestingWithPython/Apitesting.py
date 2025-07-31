import os

from playwright.async_api import async_playwright,Playwright
import pytest
import asyncio
from Models.Products_Response import productsResponse
from dotenv import load_dotenv
load_dotenv()

@pytest.mark.asyncio
async def test_get_userdata():
    async with async_playwright() as playwright:
        context = await playwright.request.new_context(base_url=os.getenv("BASEURL_GETREQUEST"))
        response = await context.get("/products")
        assert response.status == 200
        json_data = await response.json()
        ids=[]
        names=[]
        products=json_data["products"]
        for i in range(len(products)):
            productList=products[i]
            ids.append(productList["id"])

        for i in range(len(products)):
            productList=products[i]
            names.append(productList["title"])

        for i in range(len(ids)):
            productsResponse.id=ids[i]
            print(productsResponse.id)



        productsname=productList["title"]
        productsResponse.name=names[2]
        print(productsResponse.name)