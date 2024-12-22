# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class Breadcrumb(BaseElement):
    def __init__(self, locator_reader, element_key):
        super(Breadcrumb, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "Breadcrumb"

    def is_breadcrumb_active(self):
        return "active" in self.get_attribute("class")

    def is_breadcrumb__not_active(self):
        return "active" not in self.get_attribute("class")
