# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class LoadMoreButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(LoadMoreButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "LoadMoreButton"

    def is_button_loading(self):
        return "button_loading" in self.get_elements()[1].get_attribute("class")

    def is_button_disabled(self):
        return self.get_elements()[2].get_attribute("disabled")

    def is_button_load_more(self):
        return "load-more-button" in self.get_elements()[0].get_attribute("class")