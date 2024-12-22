# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class SmartPassButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(SmartPassButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "SmartPassButton"

    def is_button_large(self):
        return "button_large" in self.get_attribute("class")

    def is_button_disabled(self):
        return "disabled" in self.get_elements()[1].get_attribute("class")