from dls_auto.elements.others.SocialSharePanel import SocialSharePanel
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SocialSharePanelPage(BasePage):
    page_name = "Social Share Panel Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "social_share_panel_page_locator")
    social_share_panel = SocialSharePanel(locator_reader, "social_share_panel", "btn_apple", "btn_envelope",
                                          "btn_envelope_0", "btn_facebook", "btn_google", "btn_more")

    def __init__(self):
        super(SocialSharePanelPage, self).__init__(self.page_element)

