import random
import allure
import pytest
import os
from config.data import Data
from base.base_test import BaseTest
from dotenv import load_dotenv

load_dotenv()

@allure.feature("Profile functionality")
class TestProfileFeatureTest(BaseTest):
    @allure.title("Change profile details")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        new_name = f"Sergiusz{random.randint(1, 100)}"
        username= Data.LOGIN
        password = Data.PASSWORD

        self.login_page.open()
        self.login_page.enter_login(username)
        self.login_page.enter_password(password)
        self.login_page.click_submit()

        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_menu()

        self.my_info_page.is_opened()
        self.my_info_page.change_name(new_name)
        self.my_info_page.save_changes()
        self.my_info_page.check_changes_saved(new_name)
        self.my_info_page.make_screenshot("report_screenshot.png")
        print("test completed")
