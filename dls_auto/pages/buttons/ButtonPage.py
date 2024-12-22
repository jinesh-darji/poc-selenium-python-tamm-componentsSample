from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ButtonPage(BasePage):
    page_name = "Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "button_page_locator")
    btn_default = Button(locator_reader, "btn_default")
    btn_primary = Button(locator_reader, "btn_primary")
    btn_secondary = Button(locator_reader, "btn_secondary")
    btn_text = Button(locator_reader, "btn_text")
    btn_text_secondary = Button(locator_reader, "btn_text_secondary")
    btn_print = Button(locator_reader, "btn_print")

    def __init__(self):
        super(ButtonPage, self).__init__(self.page_element)

    def check_btn_default_has_correct_class(self):
        return self.btn_default.is_button_default()

    def check_btn_primary_has_correct_class(self):
        return self.btn_primary.is_button_primary()

    def check_btn_secondary_has_correct_class(self):
        return self.btn_secondary.is_button_secondary()

    def check_btn_text_has_correct_class(self):
        return self.btn_text.is_button_text()

    def check_btn_text_secondary_has_correct_class(self):
        return self.btn_text_secondary.is_button_text_secondary()

    def check_btn_print_has_correct_class(self):
        return self.btn_print.is_button_print()