from locators.auth_locators import AuthLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    def open_login(self) -> None:
        self.open("/login")

    def open_forgot_password(self) -> None:
        self.open("/forgot-password")

    def click_recover_password_link(self) -> None:
        self.click(AuthLocators.RECOVER_PASSWORD_LINK)
        self.wait_path_contains("/forgot-password")

    def submit_recovery_email(self, email: str) -> None:
        self.find_visible(AuthLocators.EMAIL_INPUT).send_keys(email)
        self.click(AuthLocators.RECOVER_BUTTON)
        self.wait_path_contains("/reset-password")
        self.wait_until_loaded()

    def type_reset_password(self, password: str) -> None:
        self.find_visible(AuthLocators.PASSWORD_INPUT).send_keys(password)

    def click_password_visibility_icon(self) -> None:
        self.click(AuthLocators.PASSWORD_VISIBILITY_ICON)

    def is_password_input_active(self) -> bool:
        password_input = self.find_visible(AuthLocators.PASSWORD_INPUT)
        input_container = self.find_visible(AuthLocators.PASSWORD_INPUT_CONTAINER)
        return self.is_active_element(password_input) or (
            "input_status_active" in input_container.get_attribute("class")
        )

    def is_password_input_visible(self) -> bool:
        return self.find_visible(AuthLocators.PASSWORD_INPUT).is_displayed()

    def is_forgot_password_page_opened(self) -> bool:
        return self.is_current_path_contains("/forgot-password")

    def is_reset_password_page_opened(self) -> bool:
        return self.is_current_path_contains("/reset-password")
