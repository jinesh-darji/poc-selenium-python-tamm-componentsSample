# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class Tab(BaseElement):
    def __init__(self, locator_reader, element_key):
        super(Tab, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "HorizontalTab"

    def is_tab_not_selected(self):
        self.wait_until_location_stable()
        self.get_elements()[1].click()
        return self.get_attribute("aria-selected") == "false"

    def is_tab_selected(self):
        self.wait_until_location_stable()
        self.click()
        return self.get_attribute("aria-selected") == "true"

