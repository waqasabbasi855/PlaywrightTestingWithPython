from models.museum_data import MuseumData


class CanadianMuseumDirectory:
    """
    Scraper class for extracting Canadian museum data.
    """

    DATA_BLOCKS_XPATH = "//div[@class='postBlock']"
    NEXT_BUTTON_XPATH = "(//a[text()='›'])[1]"

    def __init__(self):
        self.museums_list = []

    async def get_museum_details(self, page):
        """
        Scrape museum data from paginated website using Playwright.

        :param page: Playwright page instance
        """
        for _ in range(1, 3):  # Pagination loop (adjust range as needed)
            post_blocks = await page.query_selector_all(self.DATA_BLOCKS_XPATH)

            for index in range(1, len(post_blocks) + 1):
                museum = MuseumData(title="", location="", phone="", address="")

                elements = await page.query_selector_all(
                    f"(//div[@class='postWrap'])[{index}]//div"
                )

                title_elem = await page.query_selector(
                    f"((//div[@class='postWrap'])[{index}]//div)[1]//a"
                )

                if title_elem:
                    museum.title = await title_elem.text_content()

                # Map data block divisions
                if len(elements) > 3:
                    museum.location = await elements[1].text_content()
                    museum.phone = await elements[2].text_content()
                    museum.address = await elements[3].text_content()

                self.museums_list.append(museum)

            next_button = await page.query_selector(self.NEXT_BUTTON_XPATH)
            if next_button:
                await next_button.click()
                await page.wait_for_timeout(5000)  # Consider using `wait_for_selector` instead
            else:
                break
