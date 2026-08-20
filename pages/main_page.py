from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from locators.modal_locators import ModalLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def open_main(self) -> None:
        self.open("/")
        self.find_visible(MainPageLocators.TITLE)

    def is_constructor_opened(self) -> bool:
        return self.find_visible(MainPageLocators.TITLE).is_displayed()

    def ingredient_card_by_name(self, name: str) -> WebElement:
        return self.find_visible(MainPageLocators.ingredient_card_by_name(name))

    def click_ingredient(self, name: str) -> None:
        self.ingredient_card_by_name(name).click()
        self.find_visible(ModalLocators.INGREDIENT_DETAILS_TITLE)

    def is_ingredient_details_opened(self) -> bool:
        return self.find_visible(ModalLocators.INGREDIENT_DETAILS_TITLE).is_displayed()

    def ingredient_counter(self, name: str) -> int:
        card = self.ingredient_card_by_name(name)
        try:
            counter = card.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text)
        except NoSuchElementException:
            return 0

    def drag_ingredient_to_constructor(self, name: str) -> None:
        source = self.ingredient_card_by_name(name)
        target = self.find_visible(MainPageLocators.CONSTRUCTOR)
        self.scroll_to(source)
        self.drag_and_drop_with_offset(source, target, 100, 100)
        try:
            self.wait.until(lambda _: self.ingredient_counter(name) > 0)
        except TimeoutException:
            self._html5_drag_and_drop(source, target)
            self.wait.until(lambda _: self.ingredient_counter(name) > 0)

    def _html5_drag_and_drop(self, source: WebElement, target: WebElement) -> None:
        self.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            for (const eventName of ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend']) {
                const eventTarget = eventName === 'dragstart' || eventName === 'dragend' ? source : target;
                eventTarget.dispatchEvent(new DragEvent(eventName, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer,
                }));
            }
            """,
            source,
            target,
        )

    def place_order(self) -> int:
        self.click(MainPageLocators.ORDER_BUTTON)
        self.find_visible(ModalLocators.ORDER_ID_TEXT)
        self.wait.until(
            lambda _: self.find_visible(ModalLocators.ORDER_NUMBER).text.isdigit()
            and self.find_visible(ModalLocators.ORDER_NUMBER).text != "9999"
        )
        return int(self.find_visible(ModalLocators.ORDER_NUMBER).text)

    def constructor_has_items(self) -> bool:
        return bool(self.find_all(MainPageLocators.CONSTRUCTOR_ITEMS))

    def wait_order_modal_closed(self) -> None:
        self.wait.until(EC.invisibility_of_element_located(ModalLocators.OPENED_MODAL))
