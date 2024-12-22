from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.ProfileCardPage import ProfileCardPage
from framework.browser.Browser import Browser


class TestProfileCardElement:
    def test_profile_card_element(self):
        main_page = MainPage()
        main_page.open_profile_card_page()
        main_page.btn_menu.click()
        profile_card_page = ProfileCardPage()
        Browser.scroll_to_top()
        assert_that(profile_card_page.check_is_card_profile_avatar(), "Card does not have profile avatar")
        assert_that(profile_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(profile_card_page.check_is_card_has_subtitle(), "Card does not have subtitle")
        assert_that(profile_card_page.check_is_card_has_body(), "Card does not have body")
        assert_that(profile_card_page.check_is_card_has_btn_learn_more(), "Card does not have learn more button")
