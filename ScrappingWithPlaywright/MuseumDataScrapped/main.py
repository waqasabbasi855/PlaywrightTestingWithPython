import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path
from playwright.async_api import async_playwright

from scrappers.canadianmuseumdirectory_scrapper import CanadianMuseumDirectory
from utils.csv_writer import append_dicts_to_csv

# Load environment variables
load_dotenv()

HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
START_URL = os.getenv("START_URL")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "output/museum_data.csv")


async def run_scraper():
    scraper = CanadianMuseumDirectory()

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=HEADLESS)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(START_URL)

        await scraper.get_museum_details(page)

        await browser.close()

    if scraper.museums_list:
        data_dicts = [vars(dentist) for dentist in scraper.museums_list]
        Path("output").mkdir(exist_ok=True)
        append_dicts_to_csv(data_dicts, OUTPUT_PATH)
        print(f"✅ Scraped {len(data_dicts)} museums.")
    else:
        print("❌ No museum data found.")


if __name__ == "__main__":
    asyncio.run(run_scraper())
