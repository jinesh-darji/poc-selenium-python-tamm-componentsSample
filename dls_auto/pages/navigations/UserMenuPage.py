from dls_auto.elements.navigations.UserMenu import UserMenu
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class UserMenuPage(BasePage):
    page_name = "User Menu Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "user_menu_page_locator")
    user_menu = UserMenu(locator_reader, "user_menu", "btn_notifications", "btn_exit")

    def __init__(self):
        super(UserMenuPage, self).__init__(self.page_element)

    def check_is_btn_notifications_displayed(self):
        return self.user_menu.is_btn_notifications_displayed()

    def check_is_btn_exit_displayed(self):
        return self.user_menu.is_btn_exit_displayed()
