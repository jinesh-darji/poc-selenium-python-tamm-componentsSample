# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class CookieTray(BaseElement):
    ELEMENTS_COUNT = 3

    def __init__(self, locator_reader, element_key, message, link, button):
        super(CookieTray, self).__init__(locator_reader, element_key)
        self.message = Label(locator_reader, message)
        self.link = Label(locator_reader, link)
        self.button = Button(locator_reader, button)

    def get_element_type(self):
        return "CookieTray"

    def is_tray_has_message(self):
        return self.message.is_present()

    def is_tray_has_link(self):
        return self.link.is_present()

    def is_tray_has_button(self):
        return self.button.is_present()
