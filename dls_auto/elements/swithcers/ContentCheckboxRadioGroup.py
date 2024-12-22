# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class ContentCheckboxRadioGroup(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(ContentCheckboxRadioGroup, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "ContentCheckboxRadioGroupPage"

    def is_content_checkbox_group_checked(self):
        return "ant-checkbox-checked" in self.get_elements()[0].get_attribute("class")

    def is_content_checkbox_group_unchecked(self):
        return "ant-checkbox" in self.get_elements()[1].get_attribute("class")

    def is_content_checkbox_group_unchecked_disabled(self):
        return "ant-checkbox ant-checkbox-disabled" in self.get_elements()[2].get_attribute("class")

    def is_radio_button_group_checked(self):
        return "radio-checked" in self.get_elements()[0].get_attribute("class")

    def is_radio_button_group_unchecked(self):
        return "ant-radio" in self.get_elements()[1].get_attribute("class")

    def is_radio_button_group_unchecked_disabled(self):
        return "ant-radio-disabled" in self.get_elements()[2].get_attribute("class")
