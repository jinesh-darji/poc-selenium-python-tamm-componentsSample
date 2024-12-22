# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class ActionCard(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_header_action, lbl_header_content, lbl_body_description, btn_start_now):
        super(ActionCard, self).__init__(locator_reader, element_key)
        self.lbl_header_action = Label(locator_reader, lbl_header_action)
        self.lbl_header_content = Label(locator_reader, lbl_header_content)
        self.lbl_body_description = Label(locator_reader, lbl_body_description)
        self.btn_start_now = Button(locator_reader, btn_start_now)

    def get_element_type(self):
        return "ActionCard"

    def is_card_has_header_action(self):
        return self.lbl_header_action.is_present()

    def is_card_has_header_content(self):
        return self.lbl_header_content.is_present()

    def is_card_has_body_description(self):
        return self.lbl_body_description.is_present()

    def is_card_has_btn_start_now(self):
        return self.btn_start_now.is_present()