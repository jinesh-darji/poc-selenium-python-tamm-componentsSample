from dls_auto.elements.buttons.UploadButton import UploadButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class UploadButtonPage(BasePage):
    page_name = "Upload Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "upload_button_page_locator")
    btn_upload = UploadButton(locator_reader, "btn_upload")

    def __init__(self):
        super(UploadButtonPage, self).__init__(self.page_element)

    def check_upload_button_is_present(self):
        return self.btn_upload.is_button_upload()

    def check_upload_button_is_disabled(self):
        return self.btn_upload.is_button_disabled()