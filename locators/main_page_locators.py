from selenium.webdriver.common.by import By


class MainPageLocators:
    TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    INGREDIENT_CARDS = (By.CSS_SELECTOR, "a[class*='BurgerIngredient_ingredient']")
    CONSTRUCTOR = (By.CSS_SELECTOR, "section[class*='BurgerConstructor_basket']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ' or text()='Войти в аккаунт']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class*='counter__num']")
    CONSTRUCTOR_ITEMS = (By.CSS_SELECTOR, "span[class*='BurgerConstructor_basket__listContainer'] li")
