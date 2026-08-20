from locators.base_locators import BaseLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    def go_to_constructor(self) -> None:
        self.click(BaseLocators.CONSTRUCTOR_LINK)
        self.wait_path_is("/")
        self.wait_until_loaded()

    def go_to_order_feed(self) -> None:
        self.click(BaseLocators.ORDER_FEED_LINK)
        self.wait_path_contains("/feed")
        self.wait_until_loaded()

    def is_order_feed_opened(self) -> bool:
        return self.is_current_path_contains("/feed")

    def go_to_account(self) -> None:
        self.click(BaseLocators.ACCOUNT_LINK)
        self.wait_path_contains("/account")
        self.wait_until_loaded()

    def go_to_login(self) -> None:
        self.click(BaseLocators.ACCOUNT_LINK)
        self.wait_path_contains("/login")
        self.wait_until_loaded()
