from hamcrest import assert_that

from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser
from dls_auto.pages.pickers.DateTimePickerPage import DateTimePickerPage


class TestDatePickerElement:

    def test_date_time_picker(self):
        main_page = MainPage()
        main_page.open_date_time_picker_page()
        main_page.btn_menu.click()
        date_time_picker_page = DateTimePickerPage()
        date_time_picker_page.scroll_to_element(date_time_picker_page.page_element)
        assert_that(date_time_picker_page.check_is_selected_carousel_day(), "Time selection is not visible")
        assert_that(date_time_picker_page.check_is_scrollable_right(), "Date carousel is not scrollable right")
        assert_that(date_time_picker_page.check_is_scrollable_left(), "Date carousel is not scrollable left")
