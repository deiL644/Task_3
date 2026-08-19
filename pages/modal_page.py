from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from locators.modal_locators import ModalLocators
from pages.base_page import BasePage


class ModalPage(BasePage):
    def close(self) -> None:
        self.click(ModalLocators.CLOSE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(ModalLocators.OPENED_MODAL))

    def is_opened(self) -> bool:
        try:
            return self.find_visible(ModalLocators.OPENED_MODAL).is_displayed()
        except TimeoutException:
            return False
