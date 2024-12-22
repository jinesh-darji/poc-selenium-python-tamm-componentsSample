from dls_auto.elements.forms.UploadInput import UploadInput
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class UploadInputPage(BasePage):
    page_name = "Upload Input Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "upload_input_page_locator")
    upload_input_success = UploadInput(locator_reader, "upload_input_success")
    upload_input_failure = UploadInput(locator_reader, "upload_input_failure")
    upload_input_disabled = UploadInput(locator_reader, "upload_input_disabled")

    def __init__(self):
        super(UploadInputPage, self).__init__(self.page_element)

    def check_upload_input_success_has_class(self):
        return self.upload_input_success.is_upload_input_success()

    def check_upload_input_failure_has_class(self):
        return self.upload_input_failure.is_upload_input_error()

    def check_upload_input_disabled_has_class(self):
        return self.upload_input_disabled.is_upload_input_disabled()