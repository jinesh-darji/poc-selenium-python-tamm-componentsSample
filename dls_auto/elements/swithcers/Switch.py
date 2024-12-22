# coding=utf-8
from framework.browser.Browser import Browser
from framework.elements.base.BaseElement import BaseElement


class Switch(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(Switch, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "Switch"

    def is_switch_button_unchecked(self):
        return "ant-switch" in self.get_elements()[0].get_attribute("class")

    def is_switch_button_checked(self):
        return "switch-checked" in self.get_elements()[1].get_attribute("class")

    def is_switch_button_unchecked_disabled(self):
        return "ant-switch-disabled" in self.get_elements()[2].get_attribute("class")

    def is_switch_button_checked_disabled(self):
        return "ant-switch-checked ant-switch-disabled" in self.get_elements()[3].get_attribute("class")

    def click_switch_button(self):
        Browser.scroll_to_top()
        self.wait_until_location_stable()
        self.click_js()
