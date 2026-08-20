from locators.feed_locators import FeedLocators
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def open_profile(self) -> None:
        self.open("/account")
        self.find_visible(ProfileLocators.EMAIL_INPUT)

    def go_to_order_history(self) -> None:
        self.click(ProfileLocators.ORDER_HISTORY_LINK)
        self.wait_path_contains("/account/order-history")
        self.wait_until_loaded()

    def logout(self) -> None:
        self.click(ProfileLocators.LOGOUT_BUTTON)
        self.wait_path_contains("/login")
        self.wait_until_loaded()

    def is_profile_page_opened(self) -> bool:
        return self.is_current_path_contains("/account")

    def is_order_history_page_opened(self) -> bool:
        return self.is_current_path_contains("/account/order-history")

    def is_login_page_opened(self) -> bool:
        return self.is_current_path_contains("/login")

    def email_value(self) -> str:
        return self.find_visible(ProfileLocators.EMAIL_INPUT).get_attribute("value")

    def history_order_numbers(self) -> list[int]:
        numbers = self.find_all_visible(FeedLocators.ORDER_NUMBERS)
        return [int(item.text.replace("#", "")) for item in numbers]
