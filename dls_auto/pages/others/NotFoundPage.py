from dls_auto.elements.others.NotFound import NotFound
from dls_auto.elements.others.SocialSharePanel import SocialSharePanel
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class NotFoundPage(BasePage):
    page_name = "Not Found Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "not_found_page_locator")
    not_found = NotFound(locator_reader, "not_found", "lbl_page", "lbl_code", "lbl_image", "btn_back")

    def __init__(self):
        super(NotFoundPage, self).__init__(self.page_element)

    def check_is_page_label_present(self):
        return self.not_found.is_page_label_present()

    def check_is_code_label_present(self):
        return self.not_found.is_code_label_present()

    def check_is_image_label_present(self):
        return self.not_found.is_image_label_present()

    def check_is_btn_back_redirects(self):
        return self.not_found.is_btn_back_redirects()