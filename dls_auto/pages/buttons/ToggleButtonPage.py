from dls_auto.elements.buttons.ToggleButton import ToggleButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ToggleButtonPage(BasePage):
    page_name = "Toggle Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "toggle_button_page_locator")
    btn_toggle = ToggleButton(locator_reader, "btn_toggle")

    def __init__(self):
        super(ToggleButtonPage, self).__init__(self.page_element)

    def check_toggle_button_is_toggled(self):
        return self.btn_toggle.is_button_toggled()

    def check_toggle_button_is_untoggled(self):

        return self.btn_toggle.is_button_untoggled()

    def check_toggle_button_is_disabled(self):
        return self.btn_toggle.is_button_disabled()