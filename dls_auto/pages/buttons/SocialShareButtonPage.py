from dls_auto.elements.buttons.SocialShareButton import SocialShareButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SocialShareButtonPage(BasePage):
    page_name = "Social Share Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "social_share_button_page_locator")
    btn_social_share = SocialShareButton(locator_reader, "btn_social_share")

    def __init__(self):
        super(SocialShareButtonPage, self).__init__(self.page_element)

    def check_social_share_button_exists(self):
        return self.btn_social_share.is_button_social()

    def check_social_share_button_is_disabled(self):
        return self.btn_social_share.is_button_disabled()
