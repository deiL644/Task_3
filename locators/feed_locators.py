from selenium.webdriver.common.by import By


class FeedLocators:
    TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_CARDS = (By.CSS_SELECTOR, "a[href*='/feed/'], a[href*='/account/order-history/']")
    ORDER_NUMBERS = (By.XPATH, "//a[contains(@href, '/feed/') or contains(@href, '/account/order-history/')]//p[starts-with(text(), '#')]")
    TOTAL_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p",
    )
    TODAY_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p",
    )
    IN_PROGRESS_NUMBERS = (
        By.XPATH,
        "//p[text()='В работе:']/following-sibling::ul//li",
    )
