# playwright/browser_setup.py

from playwright.async_api import async_playwright


async def launch_browser(headless: bool = True):
    """
    Launches a Chromium browser using Playwright.

    :param headless: Whether to launch the browser in headless mode.
    :return: Tuple of (browser, context, page)
    """
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=headless)
    context = await browser.new_context()
    page = await context.new_page()
    return playwright, browser, context, page


async def close_browser(playwright, browser, context, page):
    """
    Closes all Playwright browser instances safely.

    :param playwright: Playwright instance.
    :param browser: Browser instance.
    :param context: Browser context.
    :param page: Page instance.
    """
    await page.close()
    await context.close()
    await browser.close()
    await playwright.stop()
