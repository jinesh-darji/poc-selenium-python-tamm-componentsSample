from dls_auto.elements.buttons.DownloadButton import DownloadButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class DownloadButtonPage(BasePage):
    page_name = "Download Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "download_button_page_locator")
    btn_download = DownloadButton(locator_reader, "btn_download")

    def __init__(self):
        super(DownloadButtonPage, self).__init__(self.page_element)

    def check_download_button_exists(self):
        return self.btn_download.is_button_download()

    def check_button_is_disabled(self):
        return self.btn_download.is_button_disabled()