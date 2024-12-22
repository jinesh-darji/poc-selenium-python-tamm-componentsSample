from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.LoggedInProfileCardPage import LoggedInProfileCardPage
from framework.browser.Browser import Browser


class TestLoggedInProfileCardElement:
    def test_logged_in_profile_card_element(self):
        main_page = MainPage()
        main_page.open_logged_in_profile_card_page()
        main_page.btn_menu.click()
        logged_in_profile_card_page = LoggedInProfileCardPage()
        Browser.scroll_to_top()
        assert_that(logged_in_profile_card_page.check_is_card_has_btn_locker(), "Card does not have locker button")
        assert_that(logged_in_profile_card_page.check_is_card_has_btn_logout(), "Card does not have logout button")
        assert_that(logged_in_profile_card_page.check_is_card_has_btn_profile(), "Card does not have profile button")
        assert_that(logged_in_profile_card_page.check_is_btn_locker_clickable(), "Locker button is not clickable")
        assert_that(logged_in_profile_card_page.check_is_btn_logout_clickable(), "Logout button is not clickable")
        assert_that(logged_in_profile_card_page.check_is_btn_profile_clickable(), "Profile button is not clickable")
