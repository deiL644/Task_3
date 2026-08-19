from selenium.webdriver.common.by import By


class ModalLocators:
    OPENED_MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened'], div[class*='Modal_modal_opened']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    ORDER_ID_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']")
    ORDER_NUMBER = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2")
    ORDER_DETAILS_TITLE = (By.XPATH, "//p[text()='Cостав' or text()='Состав']")
