# coding=utf-8
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class LabelContentCard(BaseElement):
    ELEMENTS_COUNT = 6

    def __init__(self, locator_reader, element_key, lbl_title, lbl_body):
        super(LabelContentCard, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)

    def get_element_type(self):
        return "LabelContentCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_body(self):
        return self.lbl_body.get_elements_count() == self.ELEMENTS_COUNT

