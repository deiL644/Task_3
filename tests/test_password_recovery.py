import allure

from data import DEFAULT_PASSWORD
from pages.auth_page import AuthPage
from pages.header_page import HeaderPage


@allure.suite("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_open_recovery_page_from_login(self, driver):
        HeaderPage(driver).open("/")
        HeaderPage(driver).go_to_login()

        auth_page = AuthPage(driver)
        auth_page.click_recover_password_link()

        assert auth_page.is_forgot_password_page_opened()

    @allure.title("Ввод почты и клик по кнопке Восстановить")
    def test_submit_recovery_email_opens_reset_page(self, driver, test_user):
        auth_page = AuthPage(driver)
        auth_page.open_forgot_password()
        auth_page.submit_recovery_email(test_user["email"])

        assert auth_page.is_reset_password_page_opened()
        assert auth_page.is_password_input_visible()

    @allure.title("Клик по иконке показа пароля делает поле активным")
    def test_password_visibility_icon_activates_password_input(self, driver, test_user):
        auth_page = AuthPage(driver)
        auth_page.open_forgot_password()
        auth_page.submit_recovery_email(test_user["email"])
        auth_page.type_reset_password(DEFAULT_PASSWORD)

        auth_page.click_password_visibility_icon()

        assert auth_page.is_password_input_active()
