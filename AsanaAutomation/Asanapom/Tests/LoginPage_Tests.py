import os

import dotenv
from dotenv import load_dotenv

from Pages.LoginPage import login
from Pages.ProjectsPage import ProjectsPage
import pytest
from playwright.async_api import async_playwright


load_dotenv()
async def logintest(page):
    await page.goto(os.getenv("URL"))
    await login.Loginclick(page)
    await page.wait_for_load_state("domcontentloaded")
    await login.Emailfield(page, os.getenv("EMAIL"))
    await login.Continue_Email(page)
    await page.wait_for_selector(login.userpasswordfield)
    await login.passwordfield(page, os.getenv("PASSWORD"))
    await login.Final_Login_Button(page)

@pytest.mark.asyncio
async def test_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(os.getenv("URL"))
        await logintest(page)
        await page.close()
        await context.close()
        await browser.close()

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context()
#         page = await context.new_page()
#         await page.goto("https://asana.com")
#         await test_logintest(page)
#         # assert await ProjectPagetest(page)
#         await page.close()
        # ProjectPagetest(page)

# asyncio.run(main())





