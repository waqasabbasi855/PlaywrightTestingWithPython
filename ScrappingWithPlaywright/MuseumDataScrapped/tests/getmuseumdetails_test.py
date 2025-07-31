# tests/getmuseumdetails_test.py

import pytest
from pathlib import Path
from scrappers.canadianmuseumdirectory_scrapper import CanadianMuseumDirectory
from utils.csv_writer import append_dicts_to_csv
from Playwright.browser_setup import launch_browser, close_browser


@pytest.mark.asyncio
async def test_get_museum_details():
    """
    Test that Canadian museum data is successfully scraped
    and written to a CSV file using Playwright.
    """
    scraper = CanadianMuseumDirectory()

    playwright, browser, context, page = await launch_browser(headless=True)

    await page.goto(
        "https://museums.ca/site/aboutthecma/services/canadianmuseumdirectory?page=1"
    )
    await scraper.get_museum_details(page)

    await close_browser(playwright, browser, context, page)

    assert len(scraper.museums_list) > 0, "No museums scraped from the page."

    output_path = Path("C:/Users/muham/Documents/data.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    append_dicts_to_csv([vars(m) for m in scraper.museums_list], str(output_path))
