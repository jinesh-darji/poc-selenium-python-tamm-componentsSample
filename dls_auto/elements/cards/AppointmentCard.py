# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class AppointmentCard(BaseElement):
    ELEMENTS_COUNT = 3

    def __init__(self, locator_reader, element_key, lbl_header_content, lbl_body_header, btn_change):
        super(AppointmentCard, self).__init__(locator_reader, element_key)
        self.lbl_body_header = Label(locator_reader, lbl_body_header)
        self.lbl_header_content = Label(locator_reader, lbl_header_content)
        self.btn_change = Button(locator_reader, btn_change)

    def get_element_type(self):
        return "AppointmentCard"

    def is_card_has_header_content(self):
        return self.lbl_header_content.is_present()

    def is_card_has_body_header(self):
        return self.lbl_body_header.get_elements_count() == self.ELEMENTS_COUNT

    def is_card_has_btn_change(self):
        return self.btn_change.is_present()
