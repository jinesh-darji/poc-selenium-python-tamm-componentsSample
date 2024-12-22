from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.SmallDescriptionCardPage import SmallDescriptionCardPage
from framework.browser.Browser import Browser


class TestSmallDescriptionCardElement:
    def test_small_description_card_element(self):
        main_page = MainPage()
        main_page.open_small_description_card_page()
        main_page.btn_menu.click()
        small_description_card_page = SmallDescriptionCardPage()
        Browser.scroll_to_top()
        assert_that(small_description_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(small_description_card_page.check_is_card_has_body_desc(), "Card does not have body description")
        assert_that(small_description_card_page.check_is_card_has_btn_learn_more(), "Card does not have Learn More Button")
