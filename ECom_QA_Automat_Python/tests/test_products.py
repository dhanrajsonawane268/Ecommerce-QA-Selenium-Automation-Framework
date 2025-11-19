import pytest
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_add_product_to_cart_and_verify_count(driver, base_url):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # open and login
    login.open(base_url)
    login.login(ConfigReader.get('DEFAULT', 'username'), ConfigReader.get('DEFAULT', 'password'))
    assert inventory.is_logged_in()

    # add first visible product
    items = driver.find_elements(*InventoryPage.INVENTORY_ITEMS)
    assert len(items) > 0, "No inventory items found"
    first_name = items[0].find_element_by_class_name("inventory_item_name").text if hasattr(items[0], "find_element_by_class_name") else items[0].find_element("class name", "inventory_item_name").text

    # use page method
    inventory.add_item_to_cart(first_name)
    count = inventory.cart_count()
    assert count == 1, f"Expected cart count 1, got {count}"

    # open cart and verify product present by name (light-weight check)
    inventory.open_cart()
    # cart page minimal check: ensure item name appears in cart container
    assert first_name.lower() in driver.page_source.lower()
