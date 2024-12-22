from dls_auto.elements.swithcers.Checkbox import Checkbox
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CheckboxPage(BasePage):
    page_name = "Checkbox Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "checkbox_page_locator")

    chbx_black_color = Checkbox(locator_reader, "chbx_black_color")
    chbx_white_color = Checkbox(locator_reader, "chbx_white_color")

    def __init__(self):
        super(CheckboxPage, self).__init__(self.page_element)

    def check_checkbox_unchecked(self, checkbox_locator):
        return checkbox_locator.is_checkbox_unchecked()

    def check_checkbox_checked(self, checkbox_locator):
        return checkbox_locator.is_checkbox_checked()

    def check_checkbox_disabled(self, checkbox_locator):
        return checkbox_locator.is_checkbox_disabled()

    def check_checkbox_checked_disabled(self, checkbox_locator):
        return checkbox_locator.is_checkbox_checked_disabled()
