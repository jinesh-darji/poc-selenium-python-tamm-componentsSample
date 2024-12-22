from framework.elements.base.BaseElement import BaseElement


class SocialShareButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(SocialShareButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "SocialShareButton"

    def is_button_social(self):
        return "uil-social-share-button" in self.get_attribute("class")

    def is_button_disabled(self):
        return self.get_elements()[1].get_attribute("disabled")
