# coding=utf-8
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class ContactCard(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_title, lbl_body, lbl_area, lbl_phone, lbl_schedule,
                 lbl_website, lbl_map):
        super(ContactCard, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)
        self.lbl_area = Label(locator_reader, lbl_area)
        self.lbl_phone = Label(locator_reader, lbl_phone)
        self.lbl_schedule = Label(locator_reader, lbl_schedule)
        self.lbl_website = Label(locator_reader, lbl_website)
        self.lbl_map = Label(locator_reader, lbl_map)

    def get_element_type(self):
        return "ContactCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_body(self):
        return self.lbl_body.is_present()

    def is_card_has_area(self):
        return self.lbl_area.is_present()

    def is_card_has_phone(self):
        return self.lbl_phone.is_present()

    def is_card_has_schedule(self):
        return self.lbl_schedule.is_present()

    def is_card_has_website(self):
        return self.lbl_website.is_present()

    def is_card_has_map(self):
        return self.lbl_map.is_present()
