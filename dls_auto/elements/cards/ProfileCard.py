# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class ProfileCard(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_profile_avatar, lbl_title, lbl_subtitle, lbl_body, btn_learn_more):
        super(ProfileCard, self).__init__(locator_reader, element_key)
        self.lbl_profile_avatar = Label(locator_reader, lbl_profile_avatar)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)
        self.lbl_subtitle = Label(locator_reader, lbl_subtitle)
        self.btn_learn_more = Button(locator_reader, btn_learn_more)

    def get_element_type(self):
        return "ProfileCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_has_subtitle(self):
        return self.lbl_subtitle.is_present()

    def is_card_has_profile_avatar(self):
        return self.lbl_profile_avatar.is_present()

    def is_card_has_body(self):
        return self.lbl_body.is_present()

    def is_card_has_btn_learn_more(self):
        return self.btn_learn_more.is_present()
