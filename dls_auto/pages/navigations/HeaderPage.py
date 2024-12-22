from dls_auto.elements.navigations.Header import Header
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class HeaderPage(BasePage):
    page_name = "Header Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "header_page_locator")
    header = Header(locator_reader, "header", "btn_menu", "lbl_logo", "btn_language_switcher",
                    "btn_search", "btn_feedback", "lbl_side_menu", "lbl_feedback_slide")

    def __init__(self):
        super(HeaderPage, self).__init__(self.page_element)

    def check_is_btn_menu_present(self):
        return self.header.is_btn_menu_displayed()

    def check_is_lbl_logo_present(self):
        return self.header.is_lbl_logo_displayed()

    def check_is_btn_language_present(self):
        return self.header.is_btn_language_displayed()

    def check_is_btn_search_present(self):
        return self.header.is_btn_search_displayed()

    def check_is_btn_feedback_present(self):
        return self.header.is_btn_feedback_displayed()

    def check_is_side_menu_opened(self):
        return self.header.is_side_menu_opened()

    def check_is_feedback_slide_opened(self):
        return self.header.is_feedback_slide_opened()