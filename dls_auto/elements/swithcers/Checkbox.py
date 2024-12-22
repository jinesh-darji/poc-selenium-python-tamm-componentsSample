# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class Checkbox(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(Checkbox, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "Checkbox"

    def is_checkbox_unchecked(self):
        return "ant-checkbox" in self.get_elements()[0].get_attribute("class")

    def is_checkbox_checked(self):
        return "ant-checkbox-checked" in self.get_elements()[1].get_attribute("class")

    def is_checkbox_disabled(self):
        return "ant-checkbox-disabled" in self.get_elements()[2].get_attribute("class")

    def is_checkbox_checked_disabled(self):
        return "ant-checkbox-checked ant-checkbox-disabled" in self.get_elements()[3].get_attribute("class")
