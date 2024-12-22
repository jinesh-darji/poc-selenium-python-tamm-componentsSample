# coding=utf-8
from framework.elements.base.BaseElement import BaseElement

from framework.elements.TextBox import TextBox
from framework.elements.Label import Label
from framework.utils.DatetimeUtil import DatetimeUtil

class DatePicker(BaseElement):


    def __init__(self, locator_reader, element_key, icon_key,drpdwn_calendar_key):
        super(DatePicker, self).__init__(locator_reader, element_key)
        self.icon = Label(locator_reader,icon_key)
        self.drpdwn_calendar = Label(locator_reader,drpdwn_calendar_key)


    def get_element_type(self):
        return "DatePicker"

    def is_default_view(self):
        return "calendar-picker-icon" in self.icon.get_attribute("class")

    def is_date_selected_view(self):
        return "calendar-picker-clear" in self.icon.get_attribute("class")

    def open_dropdown_calendar(self):
        self.icon.wait_until_location_stable()
        self.icon.click_js()

    def is_drop_down_visible(self):
        return self.drpdwn_calendar.find_element()

    def is_input_date_picker_disabled(self):
        return "disabled" in self.get_attribute("class")

    def is_drop_down_not_visible(self):
        visible = True
        if not self.drpdwn_calendar.find_element():
            visible = False
        return visible

    def get_selected_date(self):
        current_date = DatetimeUtil.get_str_datetime("%Y-%m-%d")
        selected_date = self.get_attribute("value")
        # self.get_t
        if current_date == selected_date :
            return True
        else:
            return False
