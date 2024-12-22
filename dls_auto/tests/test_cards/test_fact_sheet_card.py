from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.FactSheetCardPage import FactSheetCardPage
from framework.browser.Browser import Browser


class TestFactSheetCardElement:
    def test_fact_sheet_card_element(self):
        main_page = MainPage()
        main_page.open_fact_sheet_card_page()
        main_page.btn_menu.click()
        fact_sheet_card_page = FactSheetCardPage()
        Browser.scroll_to_top()
        assert_that(fact_sheet_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(fact_sheet_card_page.check_is_card_has_body(), "Card does not have body")
        assert_that(fact_sheet_card_page.check_is_card_has_image(), "Card does not have image")
        assert_that(fact_sheet_card_page.check_is_card_has_btn_arrow(), "Card does not have arrow button")
