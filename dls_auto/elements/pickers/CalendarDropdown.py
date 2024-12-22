from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement
from framework.utils.DatetimeUtil import DatetimeUtil
import random

class CalendarDropDown(BaseElement):

    def __init__(self, locator_reader, element_key, btn_today_key, btn_prev_year, btn_prev_month, btn_next_month, btn_next_year, btn_month, btn_year,btn_day_key):
        super(CalendarDropDown, self).__init__(locator_reader, element_key)
        self.btn_today = Button(locator_reader, btn_today_key)
        self.btn_prev_year = Button(locator_reader, btn_prev_year)
        self.btn_prev_month = Button(locator_reader, btn_prev_month)
        self.btn_next_month = Button(locator_reader, btn_next_month)
        self.btn_next_year = Button(locator_reader, btn_next_year)
        self.btn_month = Button(locator_reader, btn_month)
        self.btn_year = Button(locator_reader, btn_year)
        self.btn_day = Button(locator_reader, btn_day_key)


    def get_element_type(self):
        return "CalendarDropDown"


    def set_today_date(self):
        self.btn_today.click_js()

    def set_prev_year(self):
        before_year = self.btn_year.get_text()
        self.btn_prev_year.click()
        after_year = self.btn_year.get_text()
        dif = int(before_year) - int(after_year)
        diff = False
        if dif == 1:
            diff = True
        return diff

    def set_next_year(self):
        before_year = self.btn_year.get_text()
        self.btn_next_year.click()
        after_year = self.btn_year.get_text()
        dif = int(after_year) - int(before_year)
        diff = False
        if dif == 1:
            diff = True
        return diff

    def set_prev_month(self):
        before_month = self.btn_month.get_text()
        self.btn_prev_month.click()
        after_month = self.btn_month.get_text()
        diff = True
        if before_month == after_month:
            diff = False
        return diff

    def set_next_month(self):
        before_month = self.btn_month.get_text()
        self.btn_next_month.click()
        after_month = self.btn_month.get_text()
        diff = True
        if before_month == after_month:
            diff = False
        return diff

    def set_random_day(self):
        self.btn_day.format("")
        day = self.btn_day.get_random_item_from_list()
        self.btn_day.format(day)
        print (day)
        self.btn_day.wait_until_location_stable()
        self.btn_day.click()


