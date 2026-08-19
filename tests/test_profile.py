import allure

from pages.base_page import BasePage
from pages.header_page import HeaderPage
from pages.profile_page import ProfilePage


@allure.suite("Личный кабинет")
class TestProfile:
    @allure.title("Переход в личный кабинет по клику")
    def test_open_profile_by_account_link(self, driver, test_user):
        BasePage(driver).set_auth_tokens(test_user["access_token"], test_user["refresh_token"])
        HeaderPage(driver).open("/")

        HeaderPage(driver).go_to_account()

        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page_opened()
        assert profile_page.email_value() == test_user["email"]

    @allure.title("Переход в историю заказов")
    def test_open_order_history(self, driver, test_user):
        BasePage(driver).set_auth_tokens(test_user["access_token"], test_user["refresh_token"])
        profile_page = ProfilePage(driver)
        profile_page.open_profile()

        profile_page.go_to_order_history()

        assert profile_page.is_order_history_page_opened()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, test_user):
        BasePage(driver).set_auth_tokens(test_user["access_token"], test_user["refresh_token"])
        profile_page = ProfilePage(driver)
        profile_page.open_profile()

        profile_page.logout()

        assert profile_page.is_login_page_opened()
        assert profile_page.is_access_token_absent()
