from dls_auto.elements.buttons.LoadMoreButton import LoadMoreButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class LoadMoreButtonPage(BasePage):
    page_name = "Load More Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "load_more_button_page_locator")
    btn_load_more = LoadMoreButton(locator_reader, "btn_load_more")

    def __init__(self):
        super(LoadMoreButtonPage, self).__init__(self.page_element)

    def check_load_more_button_is_active(self):
        return self.btn_load_more.is_button_load_more()

    def check_load_more_button_is_loading(self):
        return self.btn_load_more.is_button_loading()

    def check_load_more_button_is_disabled(self):
        return self.btn_load_more.is_button_disabled()