from dls_auto.elements.forms.RadioList import RadioList
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RadioListPage(BasePage):
    page_name = "Radio List Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "radio_list_page_locator")
    radio_list_item = RadioList(locator_reader, "radio_list_item")
    radio_list_lbl = RadioList(locator_reader, "radio_list_lbl")

    def __init__(self):
        super(RadioListPage, self).__init__(self.page_element)

    def check_radio_button_is_checked(self):
        self.radio_list_item.wait_until_location_stable()
        self.radio_list_item.get_elements()[0].click()
        return self.radio_list_lbl.is_radio_button_checked()

    def check_radio_button_is_unchecked(self):
        return self.radio_list_lbl.is_radio_button_unchecked()
