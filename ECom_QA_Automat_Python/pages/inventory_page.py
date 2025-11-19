from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def is_logged_in(self):
        return self.is_visible(self.APP_LOGO, timeout=5)

    def get_item_by_name(self, name):
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title.strip().lower() == name.strip().lower():
                return item
        return None

    def add_item_to_cart(self, name):
        item = self.get_item_by_name(name)
        if not item:
            raise ValueError(f"Item not found: {name}")
        button = item.find_element(By.CSS_SELECTOR, ".btn_inventory")
        button.click()

    def open_cart(self):
        self.click(self.CART_LINK)

    def cart_count(self):
        if self.is_visible(self.CART_BADGE, timeout=2):
            return int(self.get_text(self.CART_BADGE))
        return 0
