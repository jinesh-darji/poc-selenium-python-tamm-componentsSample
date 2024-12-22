from dls_auto.elements.pickers.TimePicker import TimePicker
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
import random


class TimePickerPage(BasePage):
    page_name = "Time Picker Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "time_picker_page_locator")
    time_picker_default = TimePicker(locator_reader,"time_picker_default",
                                     "time_picker_hours","time_picker_mins","time_combobox_dropdown" ,
                                     "time_picker_icon","time_picker_icon_clear")

    time_picker_disabled = TimePicker(locator_reader,"time_picker_disabled",
                                      "time_picker_hours","time_picker_mins" ,"time_combobox_dropdown",
                                      "time_picker_icon","time_picker_icon_clear" )

    def __init__(self):
        super(TimePickerPage, self).__init__(self.page_element)
        self.page_element.scroll_by_script()

    def check_is_time_picker_enabled(self):
        return self.time_picker_default.is_time_picker_enabled()

    def check_is_time_picker_disabled(self):
        return self.time_picker_disabled.is_time_picker_disabled()

    def check_is_selected_hour(self):
        return self.time_picker_default.is_hour_selected()

    def check_is_selected_min(self):
        return self.time_picker_default.is_min_selected()

    def check_is_input_cleared(self):
        return self.time_picker_default.is_input_cleared()

