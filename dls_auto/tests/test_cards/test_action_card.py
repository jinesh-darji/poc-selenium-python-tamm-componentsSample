from hamcrest import assert_that
from dls_auto.pages.cards.ActionCardPage import ActionCardPage
from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser


class TestActionCardElement:
    def test_action_card_element(self):
        main_page = MainPage()
        main_page.open_action_card_page()
        main_page.btn_menu.click()
        action_card_page = ActionCardPage()
        Browser.scroll_to_top()
        assert_that(action_card_page.check_is_card_has_header_action(), "Card does not have header action")
        assert_that(action_card_page.check_is_card_has_header_content(), "Card does not have header content")
        assert_that(action_card_page.check_is_card_has_body_description(), "Card does not have body description")
        assert_that(action_card_page.check_is_card_has_button(), "Card does not have start now button")