import allure
from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.notifications.AlertPage import AlertPage
from framework.browser.Browser import Browser


class TestAlertElement:
    def test_alert(self):
        main_page = MainPage()
        main_page.open_alert_page()
        main_page.btn_menu.click()
        alert_page = AlertPage()
        Browser.scroll_to_top()
        with allure.step("Check is info alert present"):
            assert_that(alert_page.check_is_alert_info_exist(),
                        "Info alert is not present")

        with allure.step("Check is Warning alert present"):
            assert_that(alert_page.check_is_alert_warning_exist(),
                        "Warning alert is not present")

        with allure.step("Check is success alert present"):
            assert_that(alert_page.check_is_alert_success_exist(),
                        "Success alert is not present")

        with allure.step("Check is error alert present"):
            assert_that(alert_page.check_is_alert_error_exist(),
                        "Error alert is not present")
