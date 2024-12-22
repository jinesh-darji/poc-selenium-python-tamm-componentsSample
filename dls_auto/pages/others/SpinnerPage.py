from dls_auto.elements.others.Service import Service
from dls_auto.elements.others.Spinner import Spinner
from framework.browser.Browser import Browser
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SpinnerPage(BasePage):
    page_name = "Spinner Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "spinner_page_locator")
    spinner_default = Spinner(locator_reader, "spinner_default")
    spinner_circle = Spinner(locator_reader, "spinner_circle")

    def __init__(self):
        super(SpinnerPage, self).__init__(self.page_element)

    def check_is_default_spinner_inversed(self):
        return self.spinner_default.is_spinner_inversed()

    def check_is_circle_spinner_inversed(self):
        return self.spinner_circle.is_spinner_inversed()

    def check_is_spinner_circle(self):
        return self.spinner_circle.is_spinner_circle()
