from dls_auto.elements.swithcers.ContentRadioButton import ContentRadioButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ContentRadioButtonPage(BasePage):
    page_name = "Content Radio Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "content_radio_button_page_locator")

    btn_radio_button = ContentRadioButton(locator_reader, "btn_radio_button")

    def __init__(self):
        super(ContentRadioButtonPage, self).__init__(self.page_element)

    def check_content_radio_button_checked(self):
        return self.btn_radio_button.is_content_radio_button_checked()

    def check_content_radio_button_unchecked(self):
        return self.btn_radio_button.is_content_radio_button_unchecked()

    def check_content_radio_button_unchecked_disabled(self):
        return self.btn_radio_button.is_content_radio_button_unchecked_disabled()

    def check_content_radio_button_checked_disabled(self):
        return self.btn_radio_button.is_content_radio_button_checked_disabled()
