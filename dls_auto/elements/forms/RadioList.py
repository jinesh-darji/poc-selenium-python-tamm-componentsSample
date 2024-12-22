# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class RadioList(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(RadioList, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return " RadioList"

    def is_radio_button_checked(self):
        return "checked" in self.get_attribute("class")

    def is_radio_button_unchecked(self):
        return "checked" not in self.get_attribute("class")
