from dls_auto.elements.forms.Select import Select
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SelectPage(BasePage):
    page_name = "Select Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "select_page_locator")
    select_success = Select(locator_reader, "select_success")
    select_failure = Select(locator_reader, "select_failure")
    select_disabled = Select(locator_reader, "select_disabled")

    def __init__(self):
        super(SelectPage, self).__init__(self.page_element)

    def check_select_success_has_class(self):
        return self.select_success.is_select_success()

    def check_select_failure_has_class(self):
        return self.select_failure.is_select_error()

    def check_select_disabled_has_class(self):
        return self.select_disabled.is_select_disabled()