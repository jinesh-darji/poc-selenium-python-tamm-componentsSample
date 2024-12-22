from dls_auto.elements.swithcers.RadioButton import RadioButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RadioButtonPage(BasePage):
    page_name = "Radio Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "radio_button_page_locator")

    btn_radio_button_black_color = RadioButton(locator_reader, "btn_radio_button_black_color")
    btn_radio_button_white_color = RadioButton(locator_reader, "btn_radio_button_white_color")

    def __init__(self):
        super(RadioButtonPage, self).__init__(self.page_element)

    def check_radio_button_unchecked(self, radio_button_locator):
        return radio_button_locator.is_radio_button_unchecked()

    def check_radio_button_checked(self, radio_button_locator):
        return radio_button_locator.is_radio_button_checked()

    def check_radio_button_disabled(self, radio_button_locator):
        return radio_button_locator.is_radio_button_unchecked_disabled()

    def check_radio_button_checked_disabled(self, radio_button_locator):
        return radio_button_locator.is_radio_button_checked_disabled()