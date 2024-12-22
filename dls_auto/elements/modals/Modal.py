# coding=utf-8
import time

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.elements.base.BaseElement import BaseElement


class Modal(BaseElement):

    def __init__(self, locator_reader, element_key, lbl_footer, lbl_topper, lbl_text, btn_next, lbl_success, lbl_error, btn_ok, btn_cancel):
        super(Modal, self).__init__(locator_reader, element_key)
        self.lbl_footer = Label(locator_reader, lbl_footer)
        self.lbl_topper = Label(locator_reader, lbl_topper)
        self.lbl_text = Label(locator_reader, lbl_text)
        self.lbl_success = Label(locator_reader, lbl_success)
        self.lbl_error = Label(locator_reader, lbl_error)
        self.btn_next = Button(locator_reader, btn_next)
        self.btn_ok = Button(locator_reader, btn_ok)
        self.btn_cancel = Button(locator_reader, btn_cancel)

    def get_element_type(self):
        return "Modal"

    def is_modal_has_topper(self):
        return self.lbl_topper.is_present()

    def is_modal_has_footer(self):
        return self.lbl_footer.is_present()

    def is_modal_has_text(self):
        return self.lbl_text.is_present()

    def is_modal_has_success(self):
        return self.lbl_success.is_present()

    def is_modal_has_error(self):
        return self.lbl_error.is_present()

    def is_modal_has_button(self):
        return self.btn_next.is_present()

    def is_modal_confirm(self):
        return self.btn_ok.is_present() and self.btn_cancel.is_present()
