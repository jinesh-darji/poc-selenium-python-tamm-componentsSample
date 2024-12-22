from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.LocationCardPage import LocationCardPage
from framework.browser.Browser import Browser


class TestLocationCardElement:
    def test_location_card_element(self):
        main_page = MainPage()
        main_page.open_location_card_page()
        main_page.btn_menu.click()
        location_card_page = LocationCardPage()
        Browser.scroll_to_top()
        assert_that(location_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(location_card_page.check_is_card_has_hero_title(), "Card does not have hero title")
        assert_that(location_card_page.check_is_card_has_body(), "Card does not have body")
        assert_that(location_card_page.check_is_card_has_image(), "Card does not have image")
        assert_that(location_card_page.check_is_card_has_price(), "Card does not have Price")
        assert_that(location_card_page.check_is_card_has_btn_label(), "Card does not have label button")
