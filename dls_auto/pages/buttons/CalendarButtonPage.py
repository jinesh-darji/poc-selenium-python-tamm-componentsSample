import time

from dls_auto.elements.buttons.CalendarButton import CalendarButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CalendarButtonPage(BasePage):
    page_name = "Calendar Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "calendar_button_page_locator")
    btn_calendar = CalendarButton(locator_reader, "btn_calendar")

    def __init__(self):
        super(CalendarButtonPage, self).__init__(self.page_element)

    def check_calendar_button_exists(self):
        return self.btn_calendar.is_button_calendar()

    def check_calendar_button_collapsed(self):
        self.btn_calendar.wait_until_location_stable()
        self.btn_calendar.click()
        return self.btn_calendar.is_button_collapsed()
