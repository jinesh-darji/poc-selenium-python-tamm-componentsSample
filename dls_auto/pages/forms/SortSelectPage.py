from dls_auto.elements.forms.SortSelect import SortSelect
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SortSelectPage(BasePage):
    page_name = "Sort Select Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "sort_select_page_locator")
    sort_select = SortSelect(locator_reader, "sort_select", "sort_select_item", "btn_open_sort_select", "sort_select_input")

    def __init__(self):
        super(SortSelectPage, self).__init__(self.page_element)

    def check_sort_select_contains_selected_value(self):
        return self.sort_select.is_sort_select_contains_selected_value()