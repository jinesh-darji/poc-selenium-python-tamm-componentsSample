# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class CompareCard(BaseElement):
    BODY_COUNT = 3

    def __init__(self, locator_reader, element_key, lbl_title, lbl_body, lbl_criteria, btn_compare, chkbx_compare):
        super(CompareCard, self).__init__(locator_reader, element_key)
        self.lbl_criteria = Label(locator_reader, lbl_criteria)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)
        self.btn_compare = Button(locator_reader, btn_compare)
        self.chkbx_compare = Button(locator_reader, chkbx_compare)

    def get_element_type(self):
        return "CompareCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_body(self):
        return self.lbl_body.get_elements_count() == self.BODY_COUNT

    def is_card_has_criteria(self):
        return self.lbl_criteria.is_present()

    def is_card_has_btn_compare(self):
        return self.btn_compare.is_present()

    def is_compare_button_checked(self):
        self.chkbx_compare.click()
        return "checked" in self.btn_compare.get_attribute("class")