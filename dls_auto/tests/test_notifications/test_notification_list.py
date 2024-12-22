import allure
from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.notifications.NotificationListPage import NotificationListPage
from framework.browser.Browser import Browser


class TestNotificationListElement:
    def test_notification_list(self):
        main_page = MainPage()
        main_page.open_notification_list_page()
        main_page.btn_menu.click()
        notification__list_page = NotificationListPage()
        Browser.scroll_to_top()

        with allure.step("Check is Notifications inside the list"):
            assert_that(notification__list_page.check_is_notification_list_present(),
                        "Notifications are not inside the list")

        with allure.step("Check is Icon notification count equal to elements count"):
            assert_that(notification__list_page.check_is_notification_icon_in_list(),
                        "Icon notification count is not equal to elements count")

        with allure.step("Check is Icon notification count equal to elements count"):
            assert_that(notification__list_page.check_is_notification_button_in_list(),
                        "Button Explore More count is not equal to elements count")
