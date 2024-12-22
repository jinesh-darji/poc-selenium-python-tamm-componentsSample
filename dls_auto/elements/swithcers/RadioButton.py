# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class RadioButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(RadioButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "RadioButton"

    def is_radio_button_unchecked(self):
        return "ant-radio" in self.get_elements()[0].get_attribute("class")

    def is_radio_button_checked(self):
        return "radio-checked" in self.get_elements()[1].get_attribute("class")

    def is_radio_button_unchecked_disabled(self):
        return "ant-radio-disabled" in self.get_elements()[2].get_attribute("class")

    def is_radio_button_checked_disabled(self):
        return "ant-radio-checked ant-radio-disabled" in self.get_elements()[3].get_attribute("class")