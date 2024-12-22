from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.LabelContentCardPage import LabelContentCardPage
from framework.browser.Browser import Browser


class TestLabelContentCardElement:
    def test_label_content_card_element(self):
        main_page = MainPage()
        main_page.open_label_content_card_page()
        main_page.btn_menu.click()
        label_content_card_page = LabelContentCardPage()
        Browser.scroll_to_top()
        assert_that(label_content_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(label_content_card_page.check_is_card_has_body(), "Card does not have body")
