from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.SummaryCardPage import SummaryCardPage
from framework.browser.Browser import Browser


class TestSummaryCardElement:
    def test_summary_card_element(self):
        main_page = MainPage()
        main_page.open_summary_card_page()
        main_page.btn_menu.click()
        summary_card_page = SummaryCardPage()
        Browser.scroll_to_top()
        assert_that(summary_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(summary_card_page.check_is_card_has_subtitle(), "Card does not have subtitle")
        assert_that(summary_card_page.check_is_card_has_desc_list(), "Card does not have list of descriptions")
        assert_that(summary_card_page.check_is_card_has_description_title(), "Card does not have description title")
        assert_that(summary_card_page.check_is_card_has_desc_summary(), "Card does not have description summary")
