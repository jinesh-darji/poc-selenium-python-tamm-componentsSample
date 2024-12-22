from dls_auto.elements.others.Table import Table
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TablePage(BasePage):
    page_name = "Table Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "table_page_locator")
    table = Table(locator_reader, "table", "btn_all", "btn_enabled",
                  "btn_disabled")

    def __init__(self):
        super(TablePage, self).__init__(self.page_element)

    def check_is_all_chxkbx_checked(self):
        return self.table.is_all_chxkbx_checked()

    def check_is_all_chxkbx_unchecked(self):
        return self.table.is_all_chxkbx_unchecked()

    def check_is_disabled_not_checked(self):
        return self.table.is_disabled_not_checked()

    def check_is_enabled_checked(self):
        return self.table.is_enabled_checked()
