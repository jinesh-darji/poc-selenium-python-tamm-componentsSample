from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.navigations.EmergencyFooterPage import EmergencyFooterPage
from framework.browser.Browser import Browser


class TestEmergencyFooterElement:
    def test_emergency_footer(self):
        main_page = MainPage()
        main_page.open_emergency_footer_page()
        main_page.btn_menu.click()
        emergency_footer_page = EmergencyFooterPage()
        Browser.scroll_to_top()
        assert_that(emergency_footer_page.check_is_header_present(),
                    "Header is not present on emergency footer")

        assert_that(emergency_footer_page.check_is_police_present(),
                    "Police Info is not present on Emergency Footer")

        assert_that(emergency_footer_page.check_is_civil_present(),
                    "Civil Info is not present on Emergency Footer")

        assert_that(emergency_footer_page.check_is_electricity_present(),
                    "Electricity Info is not present on Emergency Footer")

        assert_that(emergency_footer_page.check_is_btn_view_more_present(),
                    "View More button is not present on Emergency Footer")