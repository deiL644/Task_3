from __future__ import annotations

from selenium.webdriver.remote.webelement import WebElement

from locators.feed_locators import FeedLocators
from locators.modal_locators import ModalLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def open_feed(self) -> None:
        self.open("/feed")
        self.find_visible(FeedLocators.TITLE)
        self.find_all_visible(FeedLocators.ORDER_CARDS)

    def order_cards(self) -> list[WebElement]:
        return self.find_all_visible(FeedLocators.ORDER_CARDS)

    def open_first_order(self) -> None:
        self.order_cards()[0].click()
        self.find_visible(ModalLocators.OPENED_MODAL)

    def is_order_details_opened(self) -> bool:
        return self.find_visible(ModalLocators.ORDER_DETAILS_TITLE).is_displayed()

    def order_numbers(self) -> list[int]:
        numbers = self.find_all_visible(FeedLocators.ORDER_NUMBERS)
        return [int(item.text.replace("#", "")) for item in numbers]

    def total_counter(self) -> int:
        return self._counter_value(FeedLocators.TOTAL_COUNTER)

    def today_counter(self) -> int:
        return self._counter_value(FeedLocators.TODAY_COUNTER)

    def wait_total_counter_more_than(self, value: int) -> int:
        self.wait.until(lambda _: self.total_counter() > value)
        return self.total_counter()

    def wait_today_counter_more_than(self, value: int) -> int:
        self.wait.until(lambda _: self.today_counter() > value)
        return self.today_counter()

    def wait_order_in_feed(self, order_number: int) -> bool:
        return self.wait.until(lambda _: order_number in self.order_numbers())

    def wait_order_in_progress(self, order_number: int) -> bool:
        return self.wait.until(
            lambda _: str(order_number) in self.in_progress_numbers()
        )

    def in_progress_numbers(self) -> list[str]:
        return [item.text for item in self.find_all(FeedLocators.IN_PROGRESS_NUMBERS)]

    def wait_new_order_in_progress(self, previous_numbers: list[str]) -> bool:
        return self.wait.until(
            lambda _: any(number not in previous_numbers for number in self.in_progress_numbers())
        )

    def _counter_value(self, locator: tuple[str, str]) -> int:
        raw_value = self.find_visible(locator).text
        return int(raw_value.replace(" ", ""))
