# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class Spinner(BaseElement):
    def __init__(self, locator_reader, element_key):
        super(Spinner, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "Spinner"

    def is_spinner_inversed(self):
        return "inversed" in self.get_elements()[1].get_attribute("class")

    def is_spinner_circle(self):
        return "circle" in self.get_attribute("class")
