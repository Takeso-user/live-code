from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open page {self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is open"):
            return self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, name_of_file):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name_of_file,
            attachment_type=AttachmentType.PNG
        )
