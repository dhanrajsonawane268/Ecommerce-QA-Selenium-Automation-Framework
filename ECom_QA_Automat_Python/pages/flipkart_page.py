import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlipkartPage:

    CLOSE_POPUP = (By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")
    SEARCH_BOX = (By.NAME, "q")

    FIRST_PRODUCT = (
        By.XPATH,
        "(//div[contains(@class,'_75nlfW') or contains(@class,'slAVV4')]//a)[1]"
    )

    PRODUCT_TITLES = [
        (By.CSS_SELECTOR, "span.B_NuCI"),
        (By.CSS_SELECTOR, "span.VU-ZEz"),
        (By.CSS_SELECTOR, "span.zF2qoG")
    ]

    PRODUCT_PRICES = [
        (By.CSS_SELECTOR, "div._30jeq3"),
        (By.CSS_SELECTOR, "div.Nx9bqj.CxhGGd")
    ]

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self, url):
        self.driver.get(url)
        time.sleep(3)
        self.close_popup()

    def close_popup(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(self.CLOSE_POPUP)
            )
            btn.click()
        except:
            pass

    def search(self, text):
        box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        box.send_keys(text)
        box.submit()
        time.sleep(3)

    def open_first_product(self):
        self.close_popup()

        product = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", product)

        time.sleep(2)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

    def get_title(self):
        for loc in self.PRODUCT_TITLES:
            try:
                ele = self.wait.until(EC.visibility_of_element_located(loc))
                return ele.text.strip()
            except:
                continue
        return "Title Not Found"

    def get_price(self):
        for loc in self.PRODUCT_PRICES:
            try:
                ele = self.wait.until(EC.visibility_of_element_located(loc))
                return ele.text.strip()
            except:
                continue
        return "Price Not Found"

    def scroll_page(self, px=600):
        self.driver.execute_script(f"window.scrollBy(0,{px});")
        time.sleep(1)

    def take_screenshot(self, name):
        self.driver.save_screenshot(name)
