# coding=utf-8
import time

from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class Tag(BaseElement):
    def __init__(self, locator_reader, element_key, btn_close):
        super(Tag, self).__init__(locator_reader, element_key)
        self.btn_close = Button(locator_reader, btn_close)

    def get_element_type(self):
        return "Tag"

    def is_tag_closed(self):
        count = self.get_elements_count()
        self.btn_close.wait_until_location_stable()
        self.btn_close.click()
        self.wait_until_location_stable()
        return count - self.get_elements_count() == 1
