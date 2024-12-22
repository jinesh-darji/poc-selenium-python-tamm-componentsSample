from dls_auto.elements.forms.ButtonDropdown import ButtonDropdown
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from dls_auto.elements.forms.TextArea import TextArea


class FormPage(BasePage):
    page_name = "Form Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "form_page_locator")

    input_default = TextBox(locator_reader,"input_default")
    input_success = TextBox(locator_reader, "input_success")
    input_error = TextBox(locator_reader, "input_error")
    input_disabled = TextBox(locator_reader, "input_disabled")

    textarea_default = TextArea(locator_reader,"textarea_default")
    textarea_success = TextArea(locator_reader,"textarea_success")
    textarea_error = TextArea(locator_reader,"textarea_error")
    textarea_disabled = TextArea(locator_reader,"textarea_disabled")




    def __init__(self):
        super(FormPage, self).__init__(self.page_element)

    def check_input_success_has_class(self):
        return self.input_success.is_text_box_success()

    def check_input_failure_has_class(self):
        return self.input_error.is_text_box_failure()

    def check_input_disabled_has_class(self):
        return self.input_disabled.is_text_box_disabled()

    def check_set_input_value(self):
        return self.input_default.set_input_value()

    def check_textarea_success_has_class(self):
        return self.textarea_success.is_text_area_success()

    def check_textarea_failure_has_class(self):
        return self.textarea_error.is_text_area_error()

    def check_textarea_disabled_has_class(self):
        return self.textarea_disabled.is_text_area_disabled()

    def check_set_textarea_value(self):
        return self.textarea_default.set_textarea_value()


