# coding=utf-8
from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class SocialSharePanel(BaseElement):
    def __init__(self, locator_reader, element_key, btn_apple, btn_envelope, btn_envelope_0, btn_facebook, btn_google,
                 btn_more):
        super(SocialSharePanel, self).__init__(locator_reader, element_key)
        self.btn_apple = Button(locator_reader, btn_apple)
        self.btn_envelope = Button(locator_reader, btn_envelope)
        self.btn_envelope_0 = Button(locator_reader, btn_envelope_0)
        self.btn_facebook = Button(locator_reader, btn_facebook)
        self.btn_google = Button(locator_reader, btn_google)
        self.btn_more = Button(locator_reader, btn_more)

    def get_element_type(self):
        return "SocialSharePanel"

    def is_btn_apple_present(self):
        return self.btn_apple.is_present()

    def is_btn_envelope_present(self):
        return self.btn_envelope.is_present()

    def is_btn_envelope_0_present(self):
        return self.btn_envelope_0.is_present()

    def is_btn_facebook_present(self):
        return self.btn_facebook.is_present()

    def is_btn_google_present(self):
        return self.btn_google.is_present()

    def is_btn_more_present(self):
        return self.btn_more.is_present()

    def is_btn_more_disabled(self):
        return self.btn_more.get_elements()[1].get_attribute("disabled")

    def is_btn_google_disabled(self):
        return self.btn_google.get_elements()[1].get_attribute("disabled")

    def is_btn_facebook_disabled(self):
        return self.btn_facebook.get_elements()[1].get_attribute("disabled")

    def is_btn_envelope_0_disabled(self):
        return self.btn_envelope_0.get_elements()[1].get_attribute("disabled")

    def is_btn_envelope_disabled(self):
        return self.btn_envelope.get_elements()[1].get_attribute("disabled")

    def is_btn_apple_disabled(self):
        return self.btn_apple.get_elements()[1].get_attribute("disabled")
