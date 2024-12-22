# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class EmergencyFooter(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_header, lbl_police, lbl_civil, lbl_electricity, btn_view_more):
        super(EmergencyFooter, self).__init__(locator_reader, element_key)
        self.lbl_header = Label(locator_reader, lbl_header)
        self.lbl_police = Label(locator_reader, lbl_police)
        self.lbl_civil = Label(locator_reader, lbl_civil)
        self.lbl_electricity = Label(locator_reader, lbl_electricity)
        self.btn_view_more = Button(locator_reader, btn_view_more)

    def get_element_type(self):
        return "EmergencyFooter"

    def is_header_displayed(self):
        return self.lbl_header.is_present()

    def is_civil_displayed(self):
        return self.lbl_civil.is_present()

    def is_police_displayed(self):
        return self.lbl_police.is_present()

    def is_electricity_displayed(self):
        return self.lbl_electricity.is_present()

    def is_btn_view_more_displayed(self):
        return self.btn_view_more.is_present()
