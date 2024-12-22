# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class EventCard(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_title, lbl_body, lbl_image, lbl_date, btn_learn_more):
        super(EventCard, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)
        self.lbl_image = Label(locator_reader, lbl_image)
        self.lbl_date = Label(locator_reader, lbl_date)
        self.btn_learn_more = Button(locator_reader, btn_learn_more)

    def get_element_type(self):
        return "EventCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_body(self):
        return self.lbl_body.is_present()

    def is_card_has_image(self):
        return self.lbl_image.is_present()

    def is_card_has_date(self):
        return self.lbl_date.is_present()

    def is_card_has_btn_learn_more(self):
        return self.btn_learn_more.is_present()
