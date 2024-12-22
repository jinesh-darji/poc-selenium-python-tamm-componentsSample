from dls_auto.elements.navigations.Footer import Footer
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class FooterPage(BasePage):
    page_name = "Footer Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "footer_page_locator")
    footer = Footer(locator_reader, "footer", "lbl_useful_links", "lbl_support", "lbl_follow_us",
                    "lbl_accessibility", "btn_language")

    def __init__(self):
        super(FooterPage, self).__init__(self.page_element)

    def check_is_useful_links_present(self):
        return self.footer.is_useful_links_displayed()

    def check_is_support_present(self):
        return self.footer.is_support_displayed()

    def check_is_follow_us_present(self):
        return self.footer.is_follow_us_displayed()

    def check_is_accessibility_present(self):
        return self.footer.is_accessibility_displayed()

    def check_is_btn_language_present(self):
        return self.footer.is_btn_language_displayed()
