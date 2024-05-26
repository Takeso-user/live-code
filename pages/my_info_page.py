import time

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from config.links import Links


class MyInfoPage(BasePage):
    PAGE_URL = Links.MY_INFO_PAGE

    FIRSTNAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")

    @allure.step("enter new user details")
    def change_name(self, new_name):
        with allure.step("enter new user details"):
            firstname_field = self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME_FIELD))

            # Очистить поле с помощью двойного клика и удаления
            actions = ActionChains(self.driver)
            actions.double_click(firstname_field).perform()
            firstname_field.send_keys(Keys.DELETE)
            print("Поле очищено с помощью двойного клика и удаления, проверяем...")

            # Проверить, что поле действительно пустое
            try:
                self.wait.until(self.field_value_to_be_empty(self.FIRSTNAME_FIELD))
                print("Поле действительно пустое")
            except TimeoutException:
                current_value = firstname_field.get_attribute("value")
                print(f"Поле не пустое, текущее значение: {current_value}")
                raise

            # Ввести новое имя
            firstname_field.send_keys(new_name)
            print(f"Новое имя введено: {new_name}")
            assert self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME_FIELD)).get_attribute("value") == new_name
            time.sleep(5)

    @allure.step("save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("validate the result")
    def check_changes_saved(self, new_name):
        print(f"name {new_name}")
        firstname_field = self.wait.until(EC.text_to_be_present_in_element_value(self.FIRSTNAME_FIELD, new_name))

    def field_value_to_be_empty(self, locator):
        """ Пользовательское ожидаемое условие для ожидания, когда значение поля ввода станет пустым. """

        class FieldValueToBeEmpty:
            def __init__(self, locator):
                self.locator = locator

            def __call__(self, driver):
                element = driver.find_element(*self.locator)
                return element.get_attribute("value") == ""

        return FieldValueToBeEmpty(locator)
