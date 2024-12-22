import allure
from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.notifications.CookieTrayPage import CookieTrayPage
from framework.browser.Browser import Browser


class TestCookieTrayElement:
    def test_cookie_tray(self):
        main_page = MainPage()
        main_page.open_cookie_tray_page()
        main_page.btn_menu.click()
        cookie_tray_page = CookieTrayPage()
        Browser.scroll_to_top()

        with allure.step("Check is Cookie Tray have message element"):
            assert_that(cookie_tray_page.check_is_tray_has_message(),
                        "Cookie Tray does not have message element")
        with allure.step("Check is Cookie Tray have link element"):
            assert_that(cookie_tray_page.check_is_tray_has_link(),
                        "Cookie Tray does not have link element")
        with allure.step("Check is Cookie Tray have button element"):
            assert_that(cookie_tray_page.check_is_tray_has_button(),
                        "Cookie Tray does not have button element")
