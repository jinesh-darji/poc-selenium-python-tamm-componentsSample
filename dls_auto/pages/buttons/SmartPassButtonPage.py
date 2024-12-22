from dls_auto.elements.buttons.SmartPassButton import SmartPassButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SmartPassButtonPage(BasePage):
    page_name = "Smart Pass Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "smart_pass_button_page_locator")

    btn_smart_pass_large = SmartPassButton(locator_reader, "btn_smart_pass_large")

    def __init__(self):
        super(SmartPassButtonPage, self).__init__(self.page_element)

    def check_smart_pass_button_is_large(self):
        return self.btn_smart_pass_large.is_button_large()

    def check_smart_pass_button_is_disabled(self):
        return self.btn_smart_pass_large.is_button_disabled()