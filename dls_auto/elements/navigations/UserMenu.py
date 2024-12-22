# coding=utf-8
from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class UserMenu(BaseElement):
    def __init__(self, locator_reader, element_key, btn_notifications, btn_exit):
        super(UserMenu, self).__init__(locator_reader, element_key)
        self.btn_notifications = Button(locator_reader, btn_notifications)
        self.btn_exit = Button(locator_reader, btn_exit)

    def get_element_type(self):
        return "UserMenu"

    def is_btn_notifications_displayed(self):
        return self.btn_notifications.is_present()

    def is_btn_exit_displayed(self):
        return self.btn_exit.is_present()
