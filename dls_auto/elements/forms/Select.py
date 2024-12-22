# coding=utf-8
from framework.elements.TextBox import TextBox
from framework.elements.base.BaseElement import BaseElement
from selenium.webdriver.common.keys import Keys


class Select(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(Select, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "Select"

    def is_select_success(self):
        return "has-success" in self.get_attribute("class")

    def is_select_error(self):
        return "has-error" in self.get_attribute("class")

    def is_select_disabled(self):
        return "disabled" in self.get_attribute("class")