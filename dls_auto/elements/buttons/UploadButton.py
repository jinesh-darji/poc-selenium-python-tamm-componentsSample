# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class UploadButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(UploadButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "UploadButton"

    def is_button_upload(self):
        return "uil-upload-button" in self.get_attribute("class")

    def is_button_disabled(self):
        return "uil-upload-button_disabled" in self.get_elements()[1].get_attribute("class")