# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class ToggleButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(ToggleButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "ToggleButton"

    def is_button_toggled(self):
        self.wait_until_location_stable()
        self.get_elements()[0].click()
        return "button__label_checked" in self.get_elements()[0].get_attribute("class")

    def is_button_untoggled(self):
        self.get_elements()[1].click()
        return "button__label_checked" not in self.get_elements()[1].get_attribute("class")

    def is_button_disabled(self):
        return "disabled" in self.get_elements()[2].get_attribute("class")