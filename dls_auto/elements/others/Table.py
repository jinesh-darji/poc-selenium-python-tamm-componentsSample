# coding=utf-8
from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class Table(BaseElement):
    def __init__(self, locator_reader, element_key, btn_all, btn_enabled, btn_disabled):
        super(Table, self).__init__(locator_reader, element_key)
        self.btn_all = Button(locator_reader, btn_all)
        self.btn_enabled = Button(locator_reader, btn_enabled)
        self.btn_disabled = Button(locator_reader, btn_disabled)

    def get_element_type(self):
        return "Table"

    def is_all_chxkbx_checked(self):
        self.btn_all.wait_until_location_stable()
        self.btn_all.click()
        result = True
        for elem in self.btn_enabled.get_elements():
            result = result and "checked" in elem.get_attribute("class")
        return result

    def is_all_chxkbx_unchecked(self):

        self.btn_all.wait_until_location_stable()
        self.btn_all.click()
        result = True
        for elem in self.btn_enabled.get_elements():
            result = result and "checked" not in elem.get_attribute("class")
        return result

    def is_disabled_not_checked(self):
        self.btn_disabled.click()
        return "checked" not in self.btn_disabled.get_attribute("class")

    def is_enabled_checked(self):
        self.btn_enabled.click()
        return "checked" in self.btn_enabled.get_attribute("class")