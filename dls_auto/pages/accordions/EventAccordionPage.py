from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader

from dls_auto.elements.accordions.Collapse import Collapse

class EventAccordionPage(BasePage):
    page_name = "Event Accordion Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "event_accordion_page_locator")
    accordion_element = Collapse(locator_reader,"event_accordion_element_1")
    btn_plus_minus = Button(locator_reader,"btn_plus_minus")

    def __init__(self):
        super(EventAccordionPage, self).__init__(self.page_element)

    def check_is_accordion_closed(self):

        return  self.accordion_element.is_accordion_closed()

    def check_is_accordion_opened(self):
        return  self.accordion_element.is_accordion_opened()

    def get_expansion_accordion(self):
        self.btn_plus_minus.wait_until_location_stable()
        self.btn_plus_minus.click_js()