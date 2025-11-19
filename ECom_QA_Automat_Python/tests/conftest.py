import os
import sys
import pathlib
import pytest

# ---------------------------------------------------
# FIX: Add project root to Python path (100% required)
# ---------------------------------------------------
PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))
# ---------------------------------------------------

from utils.driver_factory import create_driver
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


# Base URL fixture (FULLY FIXED)
@pytest.fixture(scope="session")
def base_url():
    url = ConfigReader.get("DEFAULT", "base_url", fallback=None)
    if not url:
        url = ConfigReader.get("Swag Labs", "base_url", fallback=None)
    return url


# WebDriver fixture
@pytest.fixture(scope="function")
def driver():
    driver = create_driver()
    yield driver
    try:
        driver.quit()
    except:
        pass


# Screenshot hook for pytest-html
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}.png"
            path = os.path.join(screenshots_dir, file_name)

            try:
                driver.save_screenshot(path)
            except Exception:
                pass

            # Attach for pytest-html report
            if hasattr(rep, "extra"):
                rep.extra.append({
                    "name": "screenshot",
                    "format": "image/png",
                    "path": path
                })
            else:
                rep.extra = [{
                    "name": "screenshot",
                    "format": "image/png",
                    "path": path
                }]
