from dls_auto.elements.others.NavLink import NavLink
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class NavLinkPage(BasePage):
    page_name = "Nav Link Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "nav_link_page_locator")
    nav_link = NavLink(locator_reader, "nav_link", "btn_back", "btn_forward", "btn_page", )

    def __init__(self):
        super(NavLinkPage, self).__init__(self.page_element)

    def check_is_btn_back_work(self):
        return self.nav_link.is_btn_back_redirects()

    def check_is_btn_forward_work(self):
        return self.nav_link.is_btn_forward_redirects()

    def check_is_btn_page_work(self):
        return self.nav_link.is_btn_page_redirects()
