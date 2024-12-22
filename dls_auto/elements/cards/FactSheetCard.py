# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class FactSheetCard(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_image, lbl_title, lbl_body, btn_arrow):
        super(FactSheetCard, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)
        self.lbl_image = Label(locator_reader, lbl_image)
        self.btn_arrow = Button(locator_reader, btn_arrow)

    def get_element_type(self):
        return "FactSheetCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_body(self):
        return self.lbl_body.is_present()

    def is_card_has_image(self):
        return self.lbl_image.is_present()

    def is_card_has_btn_arrow(self):
        return self.btn_arrow.is_present()
