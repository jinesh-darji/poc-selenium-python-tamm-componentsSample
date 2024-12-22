from dls_auto.elements.buttons.ViewAllButton import ViewAllButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ViewAllButtonPage(BasePage):
    page_name = "View All Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "view_all_button_page_locator")
    btn_view_all = ViewAllButton(locator_reader, "btn_view_all")

    def __init__(self):
        super(ViewAllButtonPage, self).__init__(self.page_element)

    def check_button_is_view_all(self):
        return self.btn_view_all.is_button_download()
