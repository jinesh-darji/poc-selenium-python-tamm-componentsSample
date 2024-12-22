from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class InputPage(BasePage):
    page_name = "Input Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "input_page_locator")
    input_success = TextBox(locator_reader, "input_success")
    input_failure = TextBox(locator_reader, "input_failure")
    input_disabled = TextBox(locator_reader, "input_disabled")

    def __init__(self):
        super(InputPage, self).__init__(self.page_element)

    def check_input_success_has_class(self):
        return self.input_success.is_text_box_success()

    def check_input_failure_has_class(self):
        return self.input_failure.is_text_box_failure()

    def check_input_disabled_has_class(self):
        return self.input_disabled.is_text_box_disabled()