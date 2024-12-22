# coding=utf-8
from framework.elements.List import List
from framework.elements.base.BaseElement import BaseElement

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.DatetimeUtil import DatetimeUtil


class TimePicker(BaseElement):
    SCROLL_COUNT = 6
    WAS_SCROLLED = False

    def __init__(self, locator_reader, element_key,hours_key,mins_key,dropdown_combo_key,icon, clear_icon):
        super(TimePicker, self).__init__(locator_reader,element_key)
        self.hours_key = Button(locator_reader, hours_key)
        self.mins_key = Button(locator_reader, mins_key)
        self.dropdown_combo_key = Button (locator_reader,dropdown_combo_key)
        self.icon = Button (locator_reader,icon)
        self.clear_icon = Button (locator_reader,clear_icon)


    def get_element_type(self):
        return "TimePicker"

    def is_time_picker_enabled(self):
        return "uil-time-picker_disabled" not in self.get_attribute("class")

    def is_time_picker_disabled(self):
        return "uil-time-picker_disabled" in self.get_attribute("class")

    def set_random_hour_min(self, hrs_min):
        hrs_min.format("")
        hrs = hrs_min.get_random_item_from_list()
        hrs_min.format(hrs)

    def is_hour_selected(self):
        self.icon.click_js()
        self.set_random_hour_min(self.hours_key)
        self.hours_key.click()
        return "ant-time-picker-panel-select-option-selected" in self.hours_key.get_attribute("class")

    def is_min_selected(self):
        self.set_random_hour_min(self.mins_key)
        self.mins_key.click()
        return "ant-time-picker-panel-select-option-selected" in self.mins_key.get_attribute("class")

    def is_input_cleared(self):
        self.clear_icon.click()
        cleared = isinstance((self.get_attribute_list("value"))[0], str)
        return  cleared
