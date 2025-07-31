import os
from models.dentist_details import DentistDetails


class DentistInformation:
    def __init__(self):
        self.searchboxfield_xpath = "//input[@id='searchboxinput']"
        self.searchbutton_xpath = "//button[@id='searchbox-searchbutton']"
        self.sponsored_dentist = "//div[@class='hHbUWd']//text()"
        self.dentistdetails_xpath = "//a[@class='hfpxzc']"
        self.dentistname_xpath = "//h1[@class='DUwDvf lfPIob']"
        self.dentistlocation_xpath = "//button[contains(@aria-label,'Address')]/div/div/div[1]"
        self.dentist_number_xpath = "//button[contains(@aria-label,'Phone')]/div/div/div[1]"
        self.dentist_website_xpath = "//div[@class='rogA2c ITvuef']"
        self.all_businesses_list = []
        self.numberofrecords_to_fetch = int(os.getenv("NUMBER_OF_BUSINESSES_TO_FETCH"))

    async def scroll_to_load_all_results(self, page):
        scrollable_div_xpath = "//div[contains(@aria-label, 'Results for')]"
        previous_height = 0

        while True:
            scroll_area = await page.query_selector(scrollable_div_xpath)
            if scroll_area is None:
                break  # fallback if sidebar is not found

            await page.evaluate('(el) => el.scrollBy(0, el.scrollHeight)', scroll_area)
            await page.wait_for_timeout(2000)

            new_height = await page.evaluate('(el) => el.scrollHeight', scroll_area)
            if new_height == previous_height:
                break
            previous_height = new_height

    async def search(self, page, search_text):
        search = await page.query_selector(self.searchboxfield_xpath)
        await search.fill(search_text)
        await search.press('Enter')
        await page.wait_for_selector(self.dentistdetails_xpath)

        # ✅ Scroll to load more dentists
        await self.scroll_to_load_all_results(page)

    async def dentistdetails_page(self, page):
        dentistdetail = await page.query_selector_all(self.dentistdetails_xpath)
        length_of_total_records = dentistdetail.__len__()
        try:
            count_records_fetched = 1
            if self.numberofrecords_to_fetch < length_of_total_records:
                for items in dentistdetail:
                    if count_records_fetched == self.numberofrecords_to_fetch+1:
                        break
                    dentistdata = DentistDetails(name="", number="", location="", website="")
                    await items.click()
                    await page.wait_for_timeout(5000)
                    await page.wait_for_selector(self.dentistname_xpath)

                    name_selector = await page.query_selector(self.dentistname_xpath)
                    name = await name_selector.text_content() if name_selector else "empty"
                    dentistdata.name = name

                    location_wait = await page.wait_for_selector(self.dentistlocation_xpath)
                    if await location_wait.is_visible():
                        location_selector = await page.query_selector(self.dentistlocation_xpath)
                        location = await location_selector.text_content()
                        dentistdata.location = location
                    else:
                        dentistdata.location = "empty"

                    number_wait = await page.wait_for_selector(self.dentist_number_xpath)
                    if await number_wait.is_visible():
                        number_selector = await page.query_selector(self.dentist_number_xpath)
                        number = await number_selector.text_content()
                        dentistdata.number = number
                    else:
                        dentistdata.number = "empty"

                    website_wait = await page.wait_for_selector(self.dentist_website_xpath)
                    if await website_wait.is_visible():
                        website_selector = await page.query_selector(self.dentist_website_xpath)
                        website = await website_selector.text_content()
                        dentistdata.website = website
                    else:
                        dentistdata.website = "empty"
                    count_records_fetched += 1
                    self.all_businesses_list.append(dentistdata)
        except Exception:
            print("Exception Message:", Exception)

