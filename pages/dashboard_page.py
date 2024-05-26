import allure
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from config.links import Links


class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE
    MY_INFO_MENU = ("xpath", "//span[text()='My Info']")

    @allure.step("Go to MyInfo menu item")
    def click_my_info_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_MENU)).click()
