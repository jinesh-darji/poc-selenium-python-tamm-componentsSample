# coding=utf-8
import random

from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class PrevNextButtons(BaseElement):
    def __init__(self, locator_reader, element_key, btn_next, btn_prev):
        super(PrevNextButtons, self).__init__(locator_reader, element_key)
        self.btn_next = Button(locator_reader, btn_next)
        self.btn_prev = Button(locator_reader, btn_prev)

    def get_element_type(self):
        return "PrevNextButtons"

    def is_next_button_disabled(self):
        return self.btn_next.get_attribute("disabled")

    def is_prev_button_disabled(self):
        return self.btn_prev.get_attribute("disabled")

    def is_next_button_present(self):
        return self.btn_next.is_present()

    def is_prev_button_present(self):
        return self.btn_prev.is_present()