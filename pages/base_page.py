from __future__ import annotations

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import BASE_URL
from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 15) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path: str = "") -> None:
        self.driver.get(f"{BASE_URL}{path}")
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        try:
            self.wait.until(EC.invisibility_of_element_located(BaseLocators.LOADER))
        except TimeoutException:
            pass

    def find_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all_visible(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        element = self.find_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script(
                """
                arguments[0].dispatchEvent(new MouseEvent('click', {
                    bubbles: true,
                    cancelable: true,
                    view: window,
                }));
                """,
                element,
            )

    def current_path(self) -> str:
        return self.driver.current_url.replace(BASE_URL, "")

    def is_current_path_contains(self, path: str) -> bool:
        return path in self.current_path()

    def wait_path_contains(self, path: str) -> bool:
        return self.wait.until(EC.url_contains(path))

    def element_text(self, locator: tuple[str, str]) -> str:
        return self.find_visible(locator).text

    def set_auth_tokens(self, access_token: str, refresh_token: str) -> None:
        self.open("/")
        self.driver.execute_script(
            "window.localStorage.setItem('accessToken', arguments[0]);"
            "window.localStorage.setItem('refreshToken', arguments[1]);",
            access_token,
            refresh_token,
        )

    def is_access_token_absent(self) -> bool:
        return self.driver.execute_script("return window.localStorage.getItem('accessToken')") is None
