import pytest
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_valid_login(driver, base_url):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    login.open(base_url)
    login.login(ConfigReader.get('DEFAULT', 'username'), ConfigReader.get('DEFAULT', 'password'))
    assert inventory.is_logged_in(), "Expected to be logged in and see inventory logo"

@pytest.mark.regression
def test_invalid_login_shows_error(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login("wronguser", "wrongpass")
    err = login.get_error()
    assert err is not None and "username and password" in err.lower() or "Epic sadface" in err or len(err)>0
