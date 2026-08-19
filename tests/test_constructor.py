import allure

from data import BUN_NAME, INGREDIENT_NAME
from pages.base_page import BasePage
from pages.feed_page import FeedPage
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.modal_page import ModalPage


@allure.suite("Основной функционал")
class TestConstructor:
    @allure.title("Переход по клику на Конструктор")
    def test_open_constructor_by_header_link(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed()

        HeaderPage(driver).go_to_constructor()

        assert MainPage(driver).is_constructor_opened()

    @allure.title("Переход по клику на Лента заказов")
    def test_open_order_feed_by_header_link(self, driver):
        MainPage(driver).open_main()
        header_page = HeaderPage(driver)

        header_page.go_to_order_feed()

        assert header_page.is_order_feed_opened()

    @allure.title("Клик по ингредиенту открывает всплывающее окно с деталями")
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()

        main_page.click_ingredient(INGREDIENT_NAME)

        assert ModalPage(driver).is_opened()
        assert main_page.is_ingredient_details_opened()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_modal_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.click_ingredient(INGREDIENT_NAME)

        ModalPage(driver).close()

        assert not ModalPage(driver).is_opened()

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    def test_ingredient_counter_increases_after_adding_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        counter_before = main_page.ingredient_counter(INGREDIENT_NAME)

        main_page.drag_ingredient_to_constructor(INGREDIENT_NAME)

        assert main_page.ingredient_counter(INGREDIENT_NAME) == counter_before + 1

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, driver, test_user):
        BasePage(driver).set_auth_tokens(test_user["access_token"], test_user["refresh_token"])
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.drag_ingredient_to_constructor(BUN_NAME)
        main_page.drag_ingredient_to_constructor(INGREDIENT_NAME)

        order_number = main_page.place_order()

        assert order_number > 0
