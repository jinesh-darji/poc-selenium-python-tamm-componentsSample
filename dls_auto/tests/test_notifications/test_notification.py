import allure
from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.notifications.NotificationPage import NotificationPage
from framework.browser.Browser import Browser


class TestNotificationElement:
    def test_notification(self):
        main_page = MainPage()
        main_page.open_notification_page()
        main_page.btn_menu.click()
        notification_page = NotificationPage()
        Browser.scroll_to_top()
        with allure.step("Check is date notification exist"):
            assert_that(notification_page.check_is_notification_date(),
                        "Date notification does not exist")

        with allure.step("Check is icon notification exist"):
            assert_that(notification_page.check_is_notification_icon(),
                        "Icon notification does not exist")

        with allure.step("Check is custom notification exist"):
            assert_that(notification_page.check_is_notification_custom(),
                        "Custom notification does not exist")
