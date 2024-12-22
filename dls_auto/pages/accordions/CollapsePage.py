from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader

from dls_auto.elements.accordions.Collapse import Collapse

class CollapsePage(BasePage):
    page_name = "Collapse Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "collapse_page_locator")
    accordion_element_transparent = Collapse(locator_reader,"collapse_element_transparent_1")
    btn_plus_minus_transparent = Button(locator_reader,"btn_plus_minus_transparent")

    accordion_element_opaque = Collapse(locator_reader,"collapse_element_opaque_1")
    btn_plus_minus_opaque = Button(locator_reader,"btn_plus_minus_opaque")


    def __init__(self):
        super(CollapsePage, self).__init__(self.page_element)

    def check_is_accordion_transparent_closed(self):
        return  self.accordion_element_transparent.is_accordion_closed()


    def check_is_accordion_transparent_opened(self):
        return  self.accordion_element_transparent.is_accordion_opened()

    def get_transparent_expansion_accordion(self):
        self.btn_plus_minus_transparent.click_js()

    def check_is_accordion_opaque_closed(self):
        return  self.accordion_element_opaque.is_accordion_closed()

    def check_is_accordion_opaque_opened(self):
        return self.accordion_element_opaque.is_accordion_opened()

    def get_opaque_expansion_accordion(self):
        self.btn_plus_minus_opaque.click_js()

