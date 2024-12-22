from hamcrest import assert_that

from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser
from dls_auto.pages.pickers.DatePickerPage import DatePickerPage


class TestDatePickerElement:

    def test_date_picker(self):
        main_page = MainPage()
        main_page.open_date_picker_page()
        main_page.btn_menu.click()
        date_picker_page = DatePickerPage()
        Browser.scroll_to_top()
        assert_that(date_picker_page.check_is_default_calendar_icon(),"Default state DatePicker element is calendar icon")
        assert_that(date_picker_page.check_is_selected_calendar_icon(),"Selected state DatePicker element is clear icon")
        assert_that(date_picker_page.check_is_disabled(),"DatePicker input is disabled")
        assert_that(date_picker_page.check_is_dropdown_visible(),"DropDown Calendar is visible")

    def test_date_picker_dropdown_calendar_today(self):
        main_page = MainPage()
        main_page.open_date_picker_page()
        main_page.btn_menu.click()
        date_picker_page = DatePickerPage()
        Browser.scroll_to_top()
        assert_that(date_picker_page.check_calendar_set_today(),"False","DropDown Calendar today date selected")
        assert_that(date_picker_page.check_date_selected(),"Selected Date is Today Date")

    def test_date_picker_dropdown_calendar_prev_year(self):
        main_page = MainPage()
        main_page.open_date_picker_page()
        main_page.btn_menu.click()
        date_picker_page = DatePickerPage()
        Browser.scroll_to_top()
        assert_that(date_picker_page.check_prev_year_selected(),"Previous Year subtracted 1 year")

    def test_date_picker_dropdown_calendar_next_year(self):
        main_page = MainPage()
        main_page.open_date_picker_page()
        main_page.btn_menu.click()
        date_picker_page = DatePickerPage()
        Browser.scroll_to_top()
        assert_that(date_picker_page.check_next_year_selected(), "Next Year added 1 year")

    def test_date_picker_dropdown_calendar_prev_month(self):
        main_page = MainPage()
        main_page.open_date_picker_page()
        main_page.btn_menu.click()
        date_picker_page = DatePickerPage()
        Browser.scroll_to_top()
        assert_that(date_picker_page.check_prev_month_selected(), "Previous Month is changed")

    def test_date_picker_dropdown_calendar_next_month(self):
        main_page = MainPage()
        main_page.open_date_picker_page()
        main_page.btn_menu.click()
        date_picker_page = DatePickerPage()
        Browser.scroll_to_top()
        assert_that(date_picker_page.check_next_month_selected(), "Next Month is changed")
        # date_picker_page.get_selected_day_from_calendar()

    def test_date_picker_dropdown_calendar_next_month(self):
        main_page = MainPage()
        main_page.open_date_picker_page()
        main_page.btn_menu.click()
        date_picker_page = DatePickerPage()
        Browser.scroll_to_top()
        assert_that(date_picker_page.get_selected_day_from_calendar(),"False", "Random Date is selected and drop down closed")
