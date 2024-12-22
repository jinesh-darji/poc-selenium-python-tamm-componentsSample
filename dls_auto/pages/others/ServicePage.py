from dls_auto.elements.others.Service import Service
from framework.browser.Browser import Browser
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ServicePage(BasePage):
    page_name = "Service Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "service_page_locator")
    service_not_found = Service(locator_reader, "service_nf", "lbl_image_nf", "lbl_title_nf", "lbl_subtitle_nf",
                                "btn_back_nf")

    def __init__(self):
        super(ServicePage, self).__init__(self.page_element)

    def check_is_title_label_present(self):
        return self.service_not_found.is_title_label_present()

    def check_is_subtitle_label_present(self):
        return self.service_not_found.is_subtitle_label_present()

    def check_is_image_label_present(self):
        return self.service_not_found.is_image_label_present()

    def check_is_btn_back_work(self):
        result = self.service_not_found.is_btn_back_work()
        if result:
            Browser.back_page()
        return result
