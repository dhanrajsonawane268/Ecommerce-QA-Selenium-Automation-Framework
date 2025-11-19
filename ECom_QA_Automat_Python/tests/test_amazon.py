from pages.amazon_page import AmazonPage
from utils.config_reader import ConfigReader
import time

def test_amazon_full_flow(driver):
    url = ConfigReader.get("AMAZON", "base_url")
    amazon = AmazonPage(driver)

    amazon.open(url)

    amazon.search("iphone 15")
    time.sleep(2)

    amazon.scroll_page(600)
    amazon.apply_sort("price-asc-rank")
    time.sleep(2)

    amazon.click_first_product()
    time.sleep(2)

    title = amazon.get_title()
    price = amazon.get_price()

    amazon.take_screenshot("amazon_product.png")

    assert len(title) > 0
    assert "₹" in price or price != "Price Not Available"
