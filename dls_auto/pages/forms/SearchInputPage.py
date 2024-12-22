from dls_auto.elements.forms.SearchInput import SearchInput
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SearchInputPage(BasePage):
    page_name = "Search Input Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "search_input_page_locator")
    search_input = SearchInput(locator_reader, "search_input")

    def __init__(self):
        super(SearchInputPage, self).__init__(self.page_element)

    def check_is_possible_to_send_keys(self):
        return self.search_input.is_possible_to_send_keys()

