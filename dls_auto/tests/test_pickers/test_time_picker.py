from hamcrest import assert_that

from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser
from dls_auto.pages.pickers.TimePickerPage import TimePickerPage


class TestDatePickerElement:

    def test_date_time_picker(self):
        main_page = MainPage()
        main_page.open_time_picker_page()
        main_page.btn_menu.click()
        time_picker_page = TimePickerPage()
        Browser.scroll_to_top()
        assert_that(time_picker_page.check_is_time_picker_disabled(), "Time Input field is disabled")
        assert_that(time_picker_page.check_is_time_picker_enabled(), "Time Input field is enabled")
        assert_that(time_picker_page.check_is_selected_hour(), "Hour is selected")
        assert_that(time_picker_page.check_is_selected_min(), "Minute is selected")
        assert_that(time_picker_page.check_is_input_cleared(), "Input field text is cleared")
