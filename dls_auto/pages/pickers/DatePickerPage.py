from dls_auto.elements.pickers.DatePicker import DatePicker
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from dls_auto.elements.pickers.CalendarDropdown import CalendarDropDown
import random

class DatePickerPage(BasePage):
    page_name = "Date Picker Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "date_picker_page_locator")


    input_date_picker_default = DatePicker(locator_reader,"input_date_picker_default","input_date_calendar_icon","input_date_calendar_dropdown")
    input_date_picker_selected = DatePicker(locator_reader, "input_date_picker_selected","input_date_calendar_icon_clear","input_date_calendar_dropdown_selected")
    input_date_calendar_disabled = DatePicker(locator_reader,"input_date_calendar_disabled","input_date_calendar_icon","input_date_calendar_dropdown")


    calendar_dropdown = CalendarDropDown(locator_reader,"input_date_calendar_dropdown","btn_today","btn_prev_year","btn_prev_month","btn_next_month","btn_next_year","btn_month","btn_year","calendar_all_rows")


    def __init__(self):
        super(DatePickerPage, self).__init__(self.page_element)

    def check_is_default_calendar_icon(self):
        return self.input_date_picker_default.is_default_view()

    def check_is_selected_calendar_icon(self):
        return self.input_date_picker_selected.is_date_selected_view()

    def get_dropdown_calendar(self):
        return self.input_date_picker_default.open_dropdown_calendar()

    def check_is_dropdown_visible(self):
        self.get_dropdown_calendar()
        return self.input_date_picker_default.is_drop_down_visible()

    def check_is_disabled(self):
        return self.input_date_calendar_disabled.is_input_date_picker_disabled()

    def check_calendar_set_today(self):
        self.get_dropdown_calendar()
        self.calendar_dropdown.set_today_date()
        return self.input_date_picker_default.is_drop_down_not_visible()

    def check_date_selected(self):
        return self.input_date_picker_default.get_selected_date()

    def check_prev_year_selected(self):
        self.get_dropdown_calendar()
        return self.calendar_dropdown.set_prev_year()

    def check_next_year_selected(self):
        self.get_dropdown_calendar()
        return self.calendar_dropdown.set_next_year()

    def check_prev_month_selected(self):
        self.get_dropdown_calendar()
        return self.calendar_dropdown.set_prev_month()

    def check_next_month_selected(self):
        self.get_dropdown_calendar()
        return self.calendar_dropdown.set_next_month()


    def get_selected_day_from_calendar(self):
        self.get_dropdown_calendar()
        self.calendar_dropdown.set_random_day()
        return self.input_date_picker_default.is_drop_down_not_visible()




