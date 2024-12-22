# coding=utf-8
from framework.elements.List import List
from framework.elements.base.BaseElement import BaseElement

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.DatetimeUtil import DatetimeUtil


class DateTimePicker(BaseElement):
    SCROLL_COUNT = 6
    WAS_SCROLLED = False

    def __init__(self, locator_reader, day_carousel_key, times_key, left_scroll_key, right_scroll_key,
                 confirm_time_key, list_of_dates_key):
        super(DateTimePicker, self).__init__(locator_reader, day_carousel_key)
        self.left_scroll = Button(locator_reader, left_scroll_key)
        self.right_scroll = Button(locator_reader, right_scroll_key)
        self.times = Button(locator_reader, times_key)
        self.day_carousel = Button(locator_reader, day_carousel_key)
        self.list_of_dates = List(locator_reader, list_of_dates_key)


        # self.day_carousel_key = Label(locator_reader,day_carousel_key)
        # self.time_key = Label(locator_reader,time_key)

    def get_element_type(self):
        return "DateTimePicker"

    def is_scrollable_left(self):
        if self.WAS_SCROLLED:
            self.SCROLL_COUNT *= 2
        dates_before_scroll = self.list_of_dates.get_elements_text()
        self.left_scroll.wait_until_location_stable()
        for i in range(self.SCROLL_COUNT):
            self.left_scroll.wait_until_location_stable()
            self.left_scroll.click()
        dates_after_scroll = self.list_of_dates.get_elements_text()
        self.WAS_SCROLLED = True
        return dates_before_scroll[0] != dates_after_scroll[0] and dates_after_scroll[-1] != dates_before_scroll[-1]

    def is_scrollable_right(self):
        if self.WAS_SCROLLED:
            self.SCROLL_COUNT *= 2
        dates_before_scroll = self.list_of_dates.get_elements_text()
        self.left_scroll.wait_until_location_stable()
        for i in range(self.SCROLL_COUNT):
            self.right_scroll.wait_until_location_stable()
            self.right_scroll.click()
        dates_after_scroll = self.list_of_dates.get_elements_text()
        self.WAS_SCROLLED = True
        return dates_before_scroll[0] != dates_after_scroll[0] and dates_after_scroll[-1] != dates_before_scroll[-1]

    def is_time_visible(self):
        return self.times.is_present()

    #
    # def is_time_disabled(self):
    #     return "disabled" not in self.times.get_attribute("disabled")
    #
    # def is_time_enabled(self):
    #     return "disabled" in self.times.get_attribute("disabled")

    def select_a_day(self):
        self.day_carousel.wait_until_location_stable()
        self.day_carousel.click()
