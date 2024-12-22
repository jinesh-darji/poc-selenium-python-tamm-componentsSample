# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class SummaryCard(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_title, lbl_subtitle, lbl_desc_list, lbl_desc, lbl_desc_large):
        super(SummaryCard, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_subtitle = Label(locator_reader, lbl_subtitle)
        self.lbl_desc_list = Label(locator_reader, lbl_desc_list)
        self.lbl_desc = Label(locator_reader, lbl_desc)
        self.lbl_desc_large = Label(locator_reader, lbl_desc_large)

    def get_element_type(self):
        return "SummaryCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_subtitle(self):
        return self.lbl_subtitle.is_present()

    def is_card_has_desc_list(self):
        return self.lbl_desc_list.is_present()

    def is_card_has_desc_title(self):
        return self.lbl_desc.is_present()

    def is_card_has_desc_summary(self):
        return self.lbl_desc_large.is_present()
