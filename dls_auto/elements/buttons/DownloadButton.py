from framework.elements.base.BaseElement import BaseElement


class DownloadButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(DownloadButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "DownloadButton"

    def is_button_download(self):
        return "uil-download-button" in self.get_elements()[0].get_attribute("class")

    def is_button_disabled(self):
        return "disabled" in self.get_elements()[1].get_attribute("class")