import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config_reader import ConfigReader

def create_driver(browser=None):
    # read defaults from config
    if not browser:
        browser = ConfigReader.get("DEFAULT", "browser", "chrome")

    headless = ConfigReader.get("DEFAULT", "headless", "False").lower() in ("true", "1", "yes")
    implicit_wait = int(ConfigReader.get("DEFAULT", "implicit_wait", 10))
    width = int(ConfigReader.get("DEFAULT", "window_width", 1366))
    height = int(ConfigReader.get("DEFAULT", "window_height", 768))

    # ⭐ No WebDriverManager – Selenium Manager handles driver automatically
    if browser.lower() == "chrome":
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        options.add_argument(f"--window-size={width},{height}")

        if headless:
            options.add_argument("--headless=new")

        # ⭐ Selenium Manager auto-detects Chrome Driver
        driver = webdriver.Chrome(options=options)

    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument(f"--width={width}")
        options.add_argument(f"--height={height}")

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(implicit_wait)
    return driver
