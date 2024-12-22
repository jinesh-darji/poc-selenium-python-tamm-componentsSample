from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.EventCardPage import EventCardPage
from framework.browser.Browser import Browser


class TestEventCardElement:
    def test_event_card_element(self):
        main_page = MainPage()
        main_page.open_event_card_page()
        main_page.btn_menu.click()
        event_card_page = EventCardPage()
        Browser.scroll_to_top()
        assert_that(event_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(event_card_page.check_is_card_has_body(), "Card does not have body")
        assert_that(event_card_page.check_is_card_has_image(), "Card does not have image")
        assert_that(event_card_page.check_is_card_has_date(), "Card does not have date")
        assert_that(event_card_page.check_is_card_has_btn_learn_more(), "Card does not have learn more button")
