from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.SmallCardPage import SmallCardPage
from framework.browser.Browser import Browser


class TestSmallCardElement:
    def test_small_card_element(self):
        main_page = MainPage()
        main_page.open_small_card_page()
        main_page.btn_menu.click()
        small_card_page = SmallCardPage()
        Browser.scroll_to_top()
        assert_that(small_card_page.check_is_card_has_card_name(), "Card does not have name")
        assert_that(small_card_page.check_is_card_has_card_desc(), "Card does not have description")
        assert_that(small_card_page.check_is_card_has_btn_learn_more(), "Card does not have Learn More Button")
