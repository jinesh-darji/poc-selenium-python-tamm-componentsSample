# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class ThemeSwitcher(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(ThemeSwitcher, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "ThemeSwitcher"

    def is_dark_btn_checked(self):
        return "checked" in self.get_elements()[0].get_attribute("class")

    def is_light_btn_checked(self):
        return "checked" in self.get_elements()[0].get_attribute("class")