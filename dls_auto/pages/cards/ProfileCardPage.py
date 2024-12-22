from dls_auto.elements.cards.ProfileCard import ProfileCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ProfileCardPage(BasePage):
    page_name = "Profile Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "profile_card_page_locator")
    profile_card = ProfileCard(locator_reader, "profile_card", "lbl_profile_avatar", "lbl_title", "lbl_subtitle",
                               "lbl_body", "btn_learn_more")

    def __init__(self):
        super(ProfileCardPage, self).__init__(self.page_element)

    def check_is_card_profile_avatar(self):
        return self.profile_card.is_card_has_profile_avatar()

    def check_is_card_has_title(self):
        return self.profile_card.is_card_has_title()

    def check_is_card_has_subtitle(self):
        return self.profile_card.is_card_has_subtitle()

    def check_is_card_has_body(self):
        return self.profile_card.is_card_has_body()

    def check_is_card_has_btn_learn_more(self):
        return self.profile_card.is_card_has_btn_learn_more()



