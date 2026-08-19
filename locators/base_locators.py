from selenium.webdriver.common.by import By


class BaseLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
    ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']/ancestor::a")
    LOADER = (By.XPATH, "//*[text()='Загрузка...']")
