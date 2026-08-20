import allure

from data import BUN_NAME, INGREDIENT_NAME
from pages.base_page import BasePage
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.modal_page import ModalPage
from pages.profile_page import ProfilePage


@allure.suite("Лента заказов")
class TestOrderFeed:
    @allure.title("Клик по заказу открывает всплывающее окно с деталями")
    def test_click_order_opens_details_modal(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed()

        feed_page.open_first_order()

        assert ModalPage(driver).is_opened()
        assert feed_page.is_order_details_opened()

    @allure.title("Заказ пользователя из истории отображается на странице Лента заказов")
    def test_user_order_from_history_appears_in_feed(self, driver, test_user, api_client):
        order_number = api_client.create_order(test_user["access_token"])
        base_page = BasePage(driver)
        base_page.set_auth_tokens(test_user["access_token"], test_user["refresh_token"])

        profile_page = ProfilePage(driver)
        profile_page.open_profile()
        profile_page.go_to_order_history()

        feed_page = FeedPage(driver)
        feed_page.open_feed()

        assert feed_page.wait_order_in_feed(order_number)

    @allure.title("При создании нового заказа счетчик Выполнено за все время увеличивается")
    def test_total_counter_increases_after_order_created(self, driver, test_user, api_client):
        feed_page = FeedPage(driver)
        feed_page.open_feed()
        counter_before = feed_page.total_counter()

        api_client.create_order(test_user["access_token"])

        assert feed_page.wait_total_counter_more_than(counter_before) == counter_before + 1

    @allure.title("При создании нового заказа счетчик Выполнено за сегодня увеличивается")
    def test_today_counter_increases_after_order_created(self, driver, test_user, api_client):
        feed_page = FeedPage(driver)
        feed_page.open_feed()
        counter_before = feed_page.today_counter()

        api_client.create_order(test_user["access_token"])

        assert feed_page.wait_today_counter_more_than(counter_before) >= counter_before + 1

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_created_order_number_appears_in_progress(self, driver, test_user):
        feed_page = FeedPage(driver)
        feed_page.open_feed()
        previous_numbers = feed_page.in_progress_numbers()

        BasePage(driver).set_auth_tokens(test_user["access_token"], test_user["refresh_token"])
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.drag_ingredient_to_constructor(BUN_NAME)
        main_page.drag_ingredient_to_constructor(INGREDIENT_NAME)

        main_page.place_order()
        ModalPage(driver).close()

        feed_page.open_feed()
        assert feed_page.wait_new_order_in_progress(previous_numbers)
