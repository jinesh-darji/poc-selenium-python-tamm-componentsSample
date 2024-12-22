from dls_auto.elements.navigations.Breadcrumb import Breadcrumb
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class BreadcrumbPage(BasePage):
    page_name = "Breadcrumb Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "breadcrumb_page_locator")
    breadcrumb = Breadcrumb(locator_reader, "breadcrumb")

    def __init__(self):
        super(BreadcrumbPage, self).__init__(self.page_element)

    def check_is_breadcrumb_not_active(self):
        return self.breadcrumb.is_breadcrumb__not_active()

    def check_is_breadcrumb_active(self):
        self.breadcrumb.wait_until_location_stable()
        self.breadcrumb.click()
        self.breadcrumb.wait_until_location_stable()
        return self.breadcrumb.is_breadcrumb_active()
