# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class Collapse(BaseElement):


    def __init__(self, locator_reader, element_key):
        super(Collapse, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "Collapse"

    def is_accordion_closed(self):
        return "ant-collapse-item-active" not in self.get_attribute("class")

    def is_accordion_opened(self):
        return "ant-collapse-item-active" in self.get_attribute("class")
