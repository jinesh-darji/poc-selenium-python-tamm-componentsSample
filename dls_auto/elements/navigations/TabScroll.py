# coding=utf-8
from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class TabScroll(BaseElement):
    def __init__(self, locator_reader, element_key, btn_scroll_left, btn_scroll_right):
        super(TabScroll, self).__init__(locator_reader, element_key)
        self.btn_scroll_left = Button(locator_reader, btn_scroll_left)
        self.btn_scroll_right = Button(locator_reader, btn_scroll_right)

    def get_element_type(self):
        return "HorizontalTabScroll"

    def is_tab_not_selected(self):
        self.get_elements()[1].click()
        return self.get_attribute("aria-selected") == "false"

    def is_tab_selected(self):
        return self.get_attribute("aria-selected") == "true"

    def is_scroll_left_disabled(self):
        return "disabled" in self.btn_scroll_left.get_attribute("class")

    def is_scroll_right_disabled(self):
        self.btn_scroll_right.click()
        return "disabled" in self.btn_scroll_right.get_attribute("class")



