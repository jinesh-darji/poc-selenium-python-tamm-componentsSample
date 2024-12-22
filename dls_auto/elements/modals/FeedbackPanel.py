# coding=utf-8
import time

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.elements.base.BaseElement import BaseElement


class FeedbackPanel(BaseElement):
    email = "natasha_pleshlun@mail.ru"
    comment = "comment"

    def __init__(self, locator_reader, element_key, btn_yes, btn_no, txb_email, txb_comment, btn_next, lbl_thanks, chkbx_phone):
        super(FeedbackPanel, self).__init__(locator_reader, element_key)
        self.btn_yes = Button(locator_reader, btn_yes)
        self.btn_no = Button(locator_reader, btn_no)
        self.txb_email = TextBox(locator_reader, txb_email)
        self.txb_comment = TextBox(locator_reader, txb_comment)
        self.btn_next = Button(locator_reader, btn_next)
        self.lbl_thanks = Label(locator_reader, lbl_thanks)
        self.chckbx_phone = Button(locator_reader, chkbx_phone)

    def get_element_type(self):
        return "FeedbackPanel"

    def is_thanks_displayed_after_yes(self):
        self.btn_yes.click()
        return self.lbl_thanks.is_present()

    def is_thanks_not_displayed_after_no(self):
        self.btn_no.click()
        return not self.lbl_thanks.is_present()

    def is_thanks_displayed_after_filling_email_and_comment(self):
        self.txb_email.click()
        self.txb_email.send_keys(self.email)
        self.txb_comment.click()
        self.txb_comment.send_keys(self.comment)
        self.chckbx_phone.click()
        self.btn_next.click()
        return self.lbl_thanks.is_present()
