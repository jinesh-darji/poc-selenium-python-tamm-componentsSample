from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.navigations.UserMenuPage import UserMenuPage
from framework.browser.Browser import Browser


class TestUserMenuElement:
    def test_user_menu(self):
        main_page = MainPage()
        main_page.open_user_menu_page()
        main_page.btn_menu.click()
        user_menu_page = UserMenuPage()
        Browser.scroll_to_top()
        assert_that(user_menu_page.check_is_btn_notifications_displayed(),
                    "Notifications Button is not displayed")

        assert_that(user_menu_page.check_is_btn_exit_displayed(),
                    "Exit Button is not displayed")
