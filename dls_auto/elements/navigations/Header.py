# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class Header(BaseElement):
    def __init__(self, locator_reader, element_key, btn_menu, lbl_logo, btn_language_switcher, btn_search,
                 btn_feedback, lbl_side_menu, lbl_feedback_slide):
        super(Header, self).__init__(locator_reader, element_key)
        self.btn_menu = Button(locator_reader, btn_menu)
        self.lbl_logo = Label(locator_reader, lbl_logo)
        self.btn_language_switcher = Button(locator_reader, btn_language_switcher)
        self.btn_search = Button(locator_reader, btn_search)
        self.btn_feedback = Button(locator_reader, btn_feedback)
        self.lbl_side_menu = Label(locator_reader, lbl_side_menu)
        self.lbl_feedback_slide = Label(locator_reader, lbl_feedback_slide)

    def get_element_type(self):
        return "Header"

    def is_btn_menu_displayed(self):
        return self.btn_menu.is_present()

    def is_lbl_logo_displayed(self):
        return self.lbl_logo.is_present()

    def is_btn_language_displayed(self):
        return self.btn_language_switcher.is_present()

    def is_btn_search_displayed(self):
        return self.btn_search.is_present()

    def is_btn_feedback_displayed(self):
        return self.btn_feedback.is_present()

    def is_side_menu_opened(self):
        self.btn_menu.wait_until_location_stable()
        self.btn_menu.click()
        result = self.lbl_side_menu.is_present()
        self.btn_menu.click()
        return result

    def is_feedback_slide_opened(self):
        self.btn_feedback.wait_until_location_stable()
        self.btn_feedback.click()
        return self.lbl_feedback_slide.is_present()



