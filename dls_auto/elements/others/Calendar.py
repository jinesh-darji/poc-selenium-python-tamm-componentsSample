# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Dropdown import Dropdown
from framework.elements.base.BaseElement import BaseElement
import datetime


class Calendar(BaseElement):
    DEFAULT_DAY = "01"
    DEFAULT_MONTH = "Jul"

    def __init__(self, locator_reader, element_key, btn_day_template, btn_month_template, btn_month_switch,
                 btn_year_switch, dropdown_year, arrow_year,
                 dropdown_month, arrow_month):
        super(Calendar, self).__init__(locator_reader, element_key)
        self.btn_day_template = Button(locator_reader, btn_day_template)
        self.btn_month_template = Button(locator_reader, btn_month_template)
        self.btn_month_switch = Button(locator_reader, btn_month_switch)
        self.btn_year_switch = Button(locator_reader, btn_year_switch)
        self.dropdown_year = Dropdown(locator_reader, dropdown_year, arrow_year)
        self.dropdown_month = Dropdown(locator_reader, dropdown_month, arrow_month)
        self.date = datetime.datetime.now()
        self.month = self.date.strftime("%B")

    def get_element_type(self):
        return "Calendar"

    def is_calendar_switched_to_year(self):
        self.btn_year_switch.click()
        self.btn_month_template.format(self.DEFAULT_MONTH)
        return self.btn_month_template.is_present()

    def is_calendar_switched_to_month(self):
        self.btn_month_switch.click()
        self.btn_day_template.format(self.DEFAULT_DAY)
        return self.btn_day_template.is_present()

    def is_possible_to_choose_date(self):
        self.btn_day_template.format(self.month)
        date = self.btn_day_template.get_random_item_from_list()
        self.btn_day_template.format(self.month + "" + date)
        self.btn_day_template.click()
        return "selected" in self.btn_day_template.get_attribute("class")

    def is_possible_to_choose_year(self):
        self.dropdown_year.click()
