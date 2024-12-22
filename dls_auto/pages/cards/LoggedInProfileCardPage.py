from dls_auto.elements.cards.LoggedInProfileCard import LoggedInProfileCard
from framework.browser.Browser import Browser
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class LoggedInProfileCardPage(BasePage):
    page_name = "Logged In Profile Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "logged_in_profile_card_page_locator")
    logged_in_profile_card = LoggedInProfileCard(locator_reader, "logged_in_profile_card", "btn_profile", "btn_locker",
                                                 "btn_logout")
    lbl_not_found = Label(locator_reader, "lbl_not_found")

    def __init__(self):
        super(LoggedInProfileCardPage, self).__init__(self.page_element)

    def check_is_card_has_btn_profile(self):
        return self.logged_in_profile_card.is_card_has_btn_profile()

    def check_is_card_has_btn_locker(self):
        return self.logged_in_profile_card.is_card_has_btn_locker()

    def check_is_card_has_btn_logout(self):
        return self.logged_in_profile_card.is_card_has_btn_logout()

    def check_is_btn_locker_clickable(self):
        self.logged_in_profile_card.btn_locker.click()
        result = self.lbl_not_found.is_present()
        if result:
            Browser.back_page()
        return result

    def check_is_btn_logout_clickable(self):
        self.logged_in_profile_card.btn_logout.click()
        result = self.lbl_not_found.is_present()
        if result:
            Browser.back_page()
        return result

    def check_is_btn_profile_clickable(self):
        self.logged_in_profile_card.btn_profile.click()
        result = self.lbl_not_found.is_present()
        if result:
            Browser.back_page()
        return result
