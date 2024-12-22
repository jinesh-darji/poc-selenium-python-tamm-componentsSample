# coding=utf-8
from framework.elements.TextBox import TextBox
from framework.elements.base.BaseElement import BaseElement
from selenium.webdriver.common.keys import Keys


class ButtonDropdown(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(ButtonDropdown, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "ButtonDropdown"

    def is_button_dropdown_opened(self):
        return "expand_less" in self.get_attribute("class")

    def is_button_dropdown_closed(self):
        return "expand_more" in self.get_attribute("class")