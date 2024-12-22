# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class TextArea(BaseElement):


    def __init__(self, locator_reader, element_key):
        super(TextArea, self).__init__(locator_reader, element_key)

    test_input = "testing"

    def get_element_type(self):
        return "TextArea"

    def is_text_area_success(self):
        return "has-success" in self.get_attribute("class")

    def is_text_area_error(self):
        return "has-error" in self.get_attribute("class")

    def is_text_area_disabled(self):
        return "disabled" in self.get_attribute("class")

    def set_textarea_value(self):
        self.send_keys(self.test_input)
        self.wait_until_location_stable()
        return self.get_text() == self.test_input