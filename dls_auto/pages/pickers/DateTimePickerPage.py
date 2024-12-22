from dls_auto.elements.pickers.DateTimePicker import DateTimePicker
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
import random


class DateTimePickerPage(BasePage):
    page_name = "Date Time Picker Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "date_time_picker_page_locator")
    date_time_picker_default = DateTimePicker(locator_reader, "date_time_picker_day_carousel",
                                              "date_time_picker_enabled_time", "date_time_picker_left_scroll",
                                              "date_time_picker_right_scroll", "date_time_picker_confirm_time",
                                              "list_of_dates")

    def __init__(self):
        super(DateTimePickerPage, self).__init__(self.page_element)
        self.page_element.scroll_by_script()

    def check_is_scrollable_left(self):
        return self.date_time_picker_default.is_scrollable_left()

    def check_is_scrollable_right(self):
        return self.date_time_picker_default.is_scrollable_right()

    def check_is_time_disabled(self):
        return self.date_time_picker_default.is_scrollable_right()

    def check_is_time_enabled(self):
        return self.date_time_picker_default.is_scrollable_right()

    def check_is_selected_carousel_day(self):
        self.date_time_picker_default.select_a_day()
        return self.date_time_picker_default.is_time_visible()
