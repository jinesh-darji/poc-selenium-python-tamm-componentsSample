# coding=utf-8
import random

from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class Pagination(BaseElement):
    PAGE_START = 1
    PAGE_MIDDLE_END = 5
    PAGE_END = 50

    def __init__(self, locator_reader, element_key, btn_next, btn_prev, btn_page, btn_between):
        super(Pagination, self).__init__(locator_reader, element_key)
        self.btn_next = Button(locator_reader, btn_next)
        self.btn_prev = Button(locator_reader, btn_prev)
        self.btn_page = Button(locator_reader, btn_page)
        self.btn_between = Button(locator_reader, btn_between)

    def get_element_type(self):
        return " Pagination"

    def is_page_active(self):
        return "ant-pagination-item-active" in self.btn_page.get_attribute("class")

    def is_prev_button_disabled(self):
        return self.btn_prev.get_attribute("aria-disabled") == "true"

    def is_next_button_disabled(self):
        return self.btn_next.get_attribute("aria-disabled") == "true"

    def click_random_page(self):
        page = random.randint(self.PAGE_START, self.PAGE_MIDDLE_END)
        self.btn_page.format(page)
        self.btn_page.wait_until_location_stable()
        self.btn_page.click()
        return self.is_page_active()

    def prev_btn_disabled_when_first_page(self):
        self.btn_page.format(self.PAGE_START)
        self.btn_page.wait_until_location_stable()
        self.btn_page.click()
        return self.is_prev_button_disabled()

    def next_btn_disabled_when_last_page(self):
        self.btn_page.format(self.PAGE_END)
        self.btn_page.wait_until_location_stable()
        self.btn_page.click()
        return self.is_next_button_disabled()

    def is_middle_navigation_work(self):
        self.btn_page.format(self.PAGE_START)
        self.btn_page.wait_until_location_stable()
        self.btn_page.click()
        self.btn_between.wait_until_location_stable()
        self.btn_between.click()
        self.btn_page.format(self.PAGE_START + self.PAGE_MIDDLE_END)
        return self.is_page_active()