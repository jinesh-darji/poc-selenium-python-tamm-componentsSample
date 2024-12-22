# coding=utf-8
from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class LoggedInProfileCard(BaseElement):
    def __init__(self, locator_reader, element_key, btn_profile, btn_locker, btn_logout):
        super(LoggedInProfileCard, self).__init__(locator_reader, element_key)
        self.btn_profile = Button(locator_reader, btn_profile)
        self.btn_locker = Button(locator_reader, btn_locker)
        self.btn_logout = Button(locator_reader, btn_logout)

    def get_element_type(self):
        return "LoggedInProfileCard"

    def is_card_has_btn_profile(self):
        return self.btn_profile.is_present()

    def is_card_has_btn_locker(self):
        return self.btn_locker.is_present()

    def is_card_has_btn_logout(self):
        return self.btn_logout.is_present()
