# coding=utf-8
import time

from framework.elements.base.BaseElement import BaseElement


class SearchInput(BaseElement):

    test_input = "test"

    def __init__(self, locator_reader, element_key):
        super(SearchInput, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "SearchInput"

    def is_possible_to_send_keys(self):
        self.send_keys(self.test_input)
        return self.get_attribute("value") == self.test_input

