# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class SmallDescriptionCard(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_title, lbl_body_desc, btn_learn_more):
        super(SmallDescriptionCard, self).__init__(locator_reader, element_key)
        self.lbl_body_desc = Label(locator_reader, lbl_body_desc)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.btn_learn_more = Button(locator_reader, btn_learn_more)

    def get_element_type(self):
        return "SmallDescriptionCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_body_desc(self):
        return self.lbl_body_desc.is_present()

    def is_card_has_btn_learn_more(self):
        return self.btn_learn_more.is_present()
