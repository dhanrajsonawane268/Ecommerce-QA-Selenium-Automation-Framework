from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os
import time

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def click(self, by_locator):
        el = self.wait.until(EC.element_to_be_clickable(by_locator))
        el.click()

    def type(self, by_locator, text, clear_first=True):
        el = self.wait.until(EC.visibility_of_element_located(by_locator))
        if clear_first:
            el.clear()
        el.send_keys(text)

    def is_visible(self, by_locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, by_locator):
        el = self.wait.until(EC.visibility_of_element_located(by_locator))
        return el.text

    def scroll_to(self, by_locator):
        el = self.find(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)

    def take_screenshot(self, name=None):
        reports_dir = os.path.join(os.getcwd(), "reports", "screenshots")
        os.makedirs(reports_dir, exist_ok=True)
        if not name:
            name = f"screenshot_{int(time.time()*1000)}.png"
        path = os.path.join(reports_dir, name)
        self.driver.save_screenshot(path)
        return path
