from dls_auto.elements.notifications.CookieTray import CookieTray
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CookieTrayPage(BasePage):
    page_name = "Cookie Tray Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "cookie_tray_page_locator")
    cookie_tray = CookieTray(locator_reader, "cookie_tray", "message", "link", "button")

    def __init__(self):
        super(CookieTrayPage, self).__init__(self.page_element)

    def check_is_tray_has_message(self):
        return self.cookie_tray.is_tray_has_message()

    def check_is_tray_has_link(self):
        return self.cookie_tray.is_tray_has_link()

    def check_is_tray_has_button(self):
        return self.cookie_tray.is_tray_has_button()
