# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class Card(BaseElement):

    def __init__(self, locator_reader, element_key, lbl_image, lbl_title, lbl_body, btn_view):
        super(Card, self).__init__(locator_reader, element_key)
        self.lbl_image = Label(locator_reader, lbl_image)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)
        self.btn_view = Button(locator_reader, btn_view)

    def get_element_type(self):
        return "Card"

    def is_card_has_image(self):
        return self.lbl_image.get_elements_count() == 1

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_body(self):
        return self.lbl_body.is_present()

    def is_card_has_btn_view(self):
        return self.btn_view.is_present()