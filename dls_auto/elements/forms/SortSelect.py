# coding=utf-8
from selenium.webdriver.common.keys import Keys

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.elements.base.BaseElement import BaseElement


class SortSelect(BaseElement):

    def __init__(self, locator_reader, element_key, items_key, open_select_key, sort_select_input_key):

        super(SortSelect, self).__init__(locator_reader, element_key)
        self.lbl_items = Label(locator_reader, items_key)
        self.btn_open_select = Button(locator_reader, open_select_key)
        self.sort_select_input = TextBox(locator_reader, sort_select_input_key)

    def get_element_type(self):
        return "SortSelect"

    def choose_value(self):
        self.btn_open_select.wait_until_location_stable()
        self.btn_open_select.click()
        item = self.lbl_items.get_random_item_from_list()
        self.sort_select_input.send_keys(item)
        self.sort_select_input.send_keys(Keys.ENTER)
        return item

    def is_sort_select_contains_selected_value(self):
        value = self.choose_value()
        return self.get_text() == value
