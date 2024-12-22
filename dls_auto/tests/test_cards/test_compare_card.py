from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.CompareCardPage import CompareCardPage
from framework.browser.Browser import Browser


class TestCompareCardElement:
    def test_compare_card_element(self):
        main_page = MainPage()
        main_page.open_compare_card_page()
        main_page.btn_menu.click()
        compare_card_page = CompareCardPage()
        Browser.scroll_to_top()
        assert_that(compare_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(compare_card_page.check_is_card_has_body(), "Card does not have body")
        assert_that(compare_card_page.check_is_card_has_criteria(), "Card does not have criteria")
        assert_that(compare_card_page.check_is_card_has_btn_compare(), "Card does not have compare button")
        assert_that(compare_card_page.check_is_card_has_btn_compare(), "Card does not have compare button")
        assert_that(compare_card_page.check_is_compare_button_checked(),
                    "Compare button does not have checked class when checked")
