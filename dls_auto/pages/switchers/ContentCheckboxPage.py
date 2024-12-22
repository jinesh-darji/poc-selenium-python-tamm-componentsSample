from dls_auto.elements.swithcers.ContentCheckbox import ContentCheckbox
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ContentCheckboxPage(BasePage):
    page_name = "Content Checkbox Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "content_checkbox_page_locator")

    chbx_content = ContentCheckbox(locator_reader, "chbx_content")

    def __init__(self):
        super(ContentCheckboxPage, self).__init__(self.page_element)

    def check_content_checkbox_checked(self, content_checkbox_locator):
        return content_checkbox_locator.is_content_checkbox_checked()

    def check_content_checkbox_unchecked(self, content_checkbox_locator):
        return content_checkbox_locator.is_content_checkbox_unchecked()

    def check_content_checkbox_disabled(self, content_checkbox_locator):
        return content_checkbox_locator.is_content_checkbox_disabled()

    def check_content_checkbox_checked_disabled(self, content_checkbox_locator):
        return content_checkbox_locator.is_content_checkbox_checked_disabled()
