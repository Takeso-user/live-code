from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_page import BasePage
from config.links import Links


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASS_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("enter login details")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("enter login password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASS_FIELD)).send_keys(password)

    @allure.step("eclick submit button")
    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
