import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlipkartPage:

    CLOSE_POPUP = (By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")
    SEARCH_BOX = (By.NAME, "q")

    PRODUCT_TITLES = [
        (By.CSS_SELECTOR, "span.B_NuCI"),
        (By.CSS_SELECTOR, "span.VU-ZEz"),
        (By.CSS_SELECTOR, "span.zF2qoG"),
    ]

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ---------------- OPEN SITE ----------------
    def open(self, url):
        self.driver.get(url)
        time.sleep(3)
        self.close_popup()

    # ---------------- CLOSE LOGIN POPUP ----------------
    def close_popup(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(self.CLOSE_POPUP)
            )
            btn.click()
        except:
            pass

    # ---------------- SEARCH PRODUCT ----------------
    def search(self, text):
        box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        box.clear()
        box.send_keys(text)
        box.submit()
        time.sleep(3)

    # ---------------- OPEN FIRST PRODUCT (FINAL + ROBUST) ----------------
    def open_first_product(self):
        self.close_popup()

        POSSIBLE_LOCATORS = [
            (By.XPATH, "(//a[contains(@href,'/p/')])[1]"),
            (By.XPATH, "(//div[@data-id]//a)[1]"),
            (By.XPATH, "(//a[contains(@class,'_1fQZEK')])[1]"),
        ]

        product = None

        for locator in POSSIBLE_LOCATORS:
            try:
                product = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )
                break
            except:
                continue

        if not product:
            raise Exception("❌ Flipkart product not found")

        # Scroll + JS click (ads / overlays avoid)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", product)

        # Handle new tab
        time.sleep(2)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

        # 🔥 IMPORTANT: price lazy-load fix
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        time.sleep(2)

    # ---------------- GET PRODUCT TITLE ----------------
    def get_title(self):
        for loc in self.PRODUCT_TITLES:
            try:
                ele = self.wait.until(
                    EC.visibility_of_element_located(loc)
                )
                return ele.text.strip()
            except:
                continue
        return "Title Not Found"

    # ---------------- GET PRODUCT PRICE (FINAL FIX) ----------------
    def get_price(self):
        PRICE_LOCATORS = [
            (By.XPATH, "//div[contains(text(),'₹')]"),
            (By.XPATH, "//span[contains(text(),'₹')]"),
            (By.CSS_SELECTOR, "div._30jeq3"),
            (By.CSS_SELECTOR, "div.Nx9bqj"),
        ]

        for loc in PRICE_LOCATORS:
            try:
                ele = self.wait.until(
                    EC.visibility_of_element_located(loc)
                )
                price = ele.text.strip()
                if "₹" in price:
                    return price
            except:
                continue

        return "Price Not Found"

    # ---------------- SCROLL PAGE ----------------
    def scroll_page(self, px=600):
        self.driver.execute_script(f"window.scrollBy(0,{px});")
        time.sleep(1)

    # ---------------- SCREENSHOT ----------------
    def take_screenshot(self, name):
        self.driver.save_screenshot(name)
