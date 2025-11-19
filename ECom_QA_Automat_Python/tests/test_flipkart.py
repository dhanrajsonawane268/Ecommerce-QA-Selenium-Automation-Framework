from pages.flipkart_page import FlipkartPage
from utils.config_reader import ConfigReader
import time

def test_flipkart_full_flow(driver):
    url = ConfigReader.get("FLIPKART", "base_url")
    flip = FlipkartPage(driver)

    flip.open(url)
    flip.search("laptop")
    time.sleep(3)

    flip.scroll_page(600)
    flip.open_first_product()
    time.sleep(3)

    title = flip.get_title()
    price = flip.get_price()

    flip.take_screenshot("flipkart_product.png")

    assert len(title) > 0
    assert "₹" in price
