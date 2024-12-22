from dls_auto.elements.navigations.EmergencyFooter import EmergencyFooter
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class EmergencyFooterPage(BasePage):
    page_name = "Emergency Footer Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "emergency_footer_page_locator")
    emergency_footer = EmergencyFooter(locator_reader, "emergency_footer", "lbl_header", "lbl_police", "lbl_civil",
                                       "lbl_electricity", "btn_view_more")

    def __init__(self):
        super(EmergencyFooterPage, self).__init__(self.page_element)

    def check_is_header_present(self):
        return self.emergency_footer.is_header_displayed()

    def check_is_police_present(self):
        return self.emergency_footer.is_police_displayed()

    def check_is_civil_present(self):
        return self.emergency_footer.is_civil_displayed()

    def check_is_electricity_present(self):
        return self.emergency_footer.is_electricity_displayed()

    def check_is_btn_view_more_present(self):
        return self.emergency_footer.is_btn_view_more_displayed()
