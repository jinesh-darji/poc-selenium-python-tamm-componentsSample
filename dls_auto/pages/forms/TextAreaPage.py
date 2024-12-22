from dls_auto.elements.forms.TextArea import TextArea
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TextAreaPage(BasePage):
    page_name = "Text Area Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "text_area_page_locator")
    text_area_success = TextArea(locator_reader, "text_area_success")
    text_area_failure = TextArea(locator_reader, "text_area_failure")
    text_area_disabled = TextArea(locator_reader, "text_area_disabled")

    def __init__(self):
        super(TextAreaPage, self).__init__(self.page_element)

    def check_text_area_success_has_class(self):
        return self.text_area_success.is_text_area_success()

    def check_text_area_failure_has_class(self):
        return self.text_area_failure.is_text_area_error()

    def check_text_area_disabled_has_class(self):
        return self.text_area_disabled.is_text_area_disabled()