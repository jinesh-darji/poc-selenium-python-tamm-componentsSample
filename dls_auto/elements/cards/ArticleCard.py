# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class ArticleCard(BaseElement):
    ELEMENTS_COUNT = 3

    def __init__(self, locator_reader, element_key, lbl_image, lbl_title, lbl_body, btn_read):
        super(ArticleCard, self).__init__(locator_reader, element_key)
        self.lbl_image = Label(locator_reader, lbl_image)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)
        self.btn_read = Button(locator_reader, btn_read)

    def get_element_type(self):
        return "ArticleCard"

    def is_card_has_image(self):
        return self.lbl_image.is_present()

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_body(self):
        return self.lbl_body.is_present()

    def is_card_has_btn_read(self):
        return self.btn_read.is_present()