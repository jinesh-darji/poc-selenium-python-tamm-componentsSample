# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class Tooltip(BaseElement):
    def __init__(self, locator_reader, element_key):
        super(Tooltip, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "Tooltip"

    def is_tooltip_shown(self):
        return "open" in self.get_attribute("class")