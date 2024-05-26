import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True, scope="function")
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver


@pytest.fixture(autouse=True, scope="session")
def setup(request, driver):
    driver.quit()