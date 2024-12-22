# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class Badge(BaseElement):
    def __init__(self, locator_reader, element_key):
        super(Badge, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "Badge"

    def is_badge_count(self):
        return "badge-count" in self.get_attribute("class")

    def is_badge_multiple(self):
        return "badge-multiple-words" in self.get_attribute("class")


