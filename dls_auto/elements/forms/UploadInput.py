# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class UploadInput(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(UploadInput, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "UploadInput"

    def is_upload_input_success(self):
        return "has-success" in self.get_attribute("class")

    def is_upload_input_error(self):
        return "has-error" in self.get_attribute("class")

    def is_upload_input_disabled(self):
        return "disabled" in self.get_attribute("class")