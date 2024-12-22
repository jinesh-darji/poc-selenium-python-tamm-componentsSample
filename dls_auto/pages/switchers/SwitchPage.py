from dls_auto.elements.swithcers.Switch import Switch
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SwitchPage(BasePage):
    page_name = "Switch Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "switch_page_locator")

    btn_switcher = Switch(locator_reader, "btn_switcher")
    btn_switch_unchecked = Switch(locator_reader, "btn_switch_unchecked")
    btn_switch_checked = Switch(locator_reader, "btn_switch_checked")

    def __init__(self):
        super(SwitchPage, self).__init__(self.page_element)

    def check_switch_button_unchecked(self):
        return self.btn_switcher.is_switch_button_unchecked()

    def check_switch_button_checked(self):
        return self.btn_switcher.is_switch_button_checked()

    def check_switch_button_unchecked_disabled(self):
        return self.btn_switcher.is_switch_button_unchecked_disabled()

    def check_switch_button_checked_disabled(self):
        return self.btn_switcher.is_switch_button_checked_disabled()

    def check_status_switch_button_changed(self, switch_locator, checked_method):
        switch_locator.click_switch_button()
        return checked_method
