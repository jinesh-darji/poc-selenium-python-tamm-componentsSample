# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class LocationCard(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_hero_title, lbl_title, lbl_body, lbl_image, lbl_price, btn_label):
        super(LocationCard, self).__init__(locator_reader, element_key)
        self.lbl_hero_title = Label(locator_reader, lbl_hero_title)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)
        self.lbl_image = Label(locator_reader, lbl_image)
        self.lbl_price = Label(locator_reader, lbl_price)
        self.btn_label = Button(locator_reader, btn_label)

    def get_element_type(self):
        return "LocationCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_hero_title(self):
        return self.lbl_hero_title.is_present()

    def is_card_has_body(self):
        return self.lbl_body.is_present()

    def is_card_has_image(self):
        return self.lbl_image.is_present()

    def is_card_has_price(self):
        return self.lbl_price.is_present()

    def is_card_has_btn_label(self):
        return self.btn_label.is_present()
