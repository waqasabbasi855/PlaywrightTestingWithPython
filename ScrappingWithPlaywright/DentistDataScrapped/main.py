import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path
from playwright.async_api import async_playwright
from scrappers.dentistdata_scrapper import DentistInformation
from utils.csv_write import append_dicts_to_csv
load_dotenv()

HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
START_URL = os.getenv("START_URL")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "output/dentists.csv")
OUTPUT_FILE = Path(OUTPUT_PATH)

# Create output folder if it doesn't exist
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)


async def run_scraper():
    scraper = DentistInformation()

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=HEADLESS)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(START_URL)
        await scraper.search(page, os.getenv("SEARCH_TERM"))
        await scraper.dentistdetails_page(page)

        await browser.close()

    if scraper.all_businesses_list:
        data_dicts = [vars(museum) for museum in scraper.all_businesses_list]

        # Ensure the parent directory exists
        Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)

        append_dicts_to_csv(data_dicts, OUTPUT_PATH)
        print(f"✅ Scraped {len(data_dicts)} dentists. File saved to {OUTPUT_FILE}")
    else:
        print("❌ No dentist data found.")


if __name__ == "__main__":
    asyncio.run(run_scraper())

