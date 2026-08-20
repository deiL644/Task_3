from selenium.webdriver.common.by import By


class AuthLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' or @type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    PASSWORD_INPUT_CONTAINER = (
        By.XPATH,
        "//input[@name='Введите новый пароль']/ancestor::div[contains(@class, 'input')][1]",
    )
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    PASSWORD_VISIBILITY_ICON = (
        By.XPATH,
        "//input[@name='Введите новый пароль']/following-sibling::*//*[name()='svg']",
    )
