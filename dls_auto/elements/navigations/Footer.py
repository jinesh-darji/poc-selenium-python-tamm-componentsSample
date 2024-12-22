# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class Footer(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_useful_links, lbl_support, lbl_follow_us, lbl_accessibility,
                 btn_language):
        super(Footer, self).__init__(locator_reader, element_key)
        self.lbl_useful_links = Label(locator_reader, lbl_useful_links)
        self.lbl_support = Label(locator_reader, lbl_support)
        self.lbl_follow_us = Label(locator_reader, lbl_follow_us)
        self.lbl_accessibility = Label(locator_reader, lbl_accessibility)
        self.btn_language = Button(locator_reader, btn_language)

    def get_element_type(self):
        return "Footer"

    def is_useful_links_displayed(self):
        return self.lbl_useful_links.is_present()

    def is_support_displayed(self):
        return self.lbl_support.is_present()

    def is_follow_us_displayed(self):
        return self.lbl_follow_us.is_present()

    def is_accessibility_displayed(self):
        return self.lbl_accessibility.is_present()

    def is_btn_language_displayed(self):
        return self.btn_language.is_present()

    
