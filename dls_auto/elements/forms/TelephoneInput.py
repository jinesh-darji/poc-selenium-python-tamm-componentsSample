# coding=utf-8
from framework.elements.TextBox import TextBox
from framework.elements.base.BaseElement import BaseElement
from selenium.webdriver.common.keys import Keys


class TelephoneInput(BaseElement):

    def __init__(self, locator_reader, element_key, code_key, phone_key):
        super(TelephoneInput, self).__init__(locator_reader, element_key)
        self.code_input = TextBox(locator_reader, code_key)
        self.phone_input = TextBox(locator_reader, phone_key)

    def get_element_type(self):
        return "TextBox"

    def get_value(self):
        return super(TelephoneInput, self).get_attribute("value")

    def clear_field(self):
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys(Keys.DELETE)

    def is_telephone_input_success(self):
        return 'has-success' in self.get_attribute("class")

    def is_telephone_input_phone_failure(self):
        self.phone_input.format(self.get_locator())
        return self.phone_input.is_present()

    def is_telephone_input_code_failure(self):
        self.code_input.format(self.get_locator())
        return self.code_input.is_present()

    def is_telephone_input_phone_code_failure(self):
        self.phone_input.format(self.get_locator())
        self.code_input.format(self.get_locator())
        return self.code_input.is_present() and self.phone_input.is_present()

    def is_telephone_input_disabled(self):
        return 'input_disabled' in self.get_attribute("class")
