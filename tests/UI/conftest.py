import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.allure import attachments


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=False)
def open_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "99.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('SELENOID_USERNAME')
    password = os.getenv('SELENOID_PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 15
    browser.open('https://zenhotels.com')

    yield browser

    attachments.add_logs(browser)
    attachments.add_screenshot(browser)
    attachments.add_html(browser)
    attachments.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function', autouse=False)
def local_browser():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.timeout = 15
    browser.open('https://zenhotels.com')

    yield browser

    browser.quit()
