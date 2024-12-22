# coding=utf-8
from framework.browser.Browser import Browser
from framework.elements.base.BaseElement import BaseElement


class NumberSelector(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(NumberSelector, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "NumberSelector"

    def click_number_selector(self):
        Browser.scroll_to_top()
        self.wait_until_location_stable()
        self.click_js()

    def is_number_selector_minus_disabled(self):
        return self.get_attribute('disabled')

    def is_number_selector_plus_disabled(self):
        return self.get_attribute("disabled")
