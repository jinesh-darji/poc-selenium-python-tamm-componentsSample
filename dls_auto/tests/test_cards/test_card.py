from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.CardPage import CardPage
from framework.browser.Browser import Browser


class TestCardElement:
    def test_card_element(self):
        main_page = MainPage()
        main_page.open_card_page()
        main_page.btn_menu.click()
        card_page = CardPage()
        Browser.scroll_to_top()
        assert_that(card_page.check_is_card_has_image(), "Card does not have background image")
        assert_that(card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(card_page.check_is_card_has_body(), "Card does not have body")
        assert_that(card_page.check_is_card_has_btn_view(), "Card does not have View Journey button")