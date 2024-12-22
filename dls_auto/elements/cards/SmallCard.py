# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class SmallCard(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_card_name, lbl_card_desc, btn_learn_more):
        super(SmallCard, self).__init__(locator_reader, element_key)
        self.lbl_card_name = Label(locator_reader, lbl_card_name)
        self.lbl_card_desc = Label(locator_reader, lbl_card_desc)
        self.btn_learn_more = Button(locator_reader, btn_learn_more)

    def get_element_type(self):
        return "SmallCard"

    def is_card_has_card_name(self):
        return self.lbl_card_name.is_present()

    def is_card_has_card_desc(self):
        return self.lbl_card_desc.is_present()

    def is_card_has_btn_learn_more(self):
        return self.btn_learn_more.is_present()
