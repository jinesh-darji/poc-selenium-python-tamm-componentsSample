from dls_auto.elements.navigations.Pagination import Pagination
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class PaginationPage(BasePage):
    page_name = "Pagination Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "pagination_page_locator")
    pagination = Pagination(locator_reader, "pagination", "btn_next", "btn_prev", "btn_page", "btn_between")

    def __init__(self):
        super(PaginationPage, self).__init__(self.page_element)

    def check_is_random_page_clicked(self):
        return self.pagination.click_random_page()

    def check_prev_btn_disabled_when_first_page(self):
        return self.pagination.prev_btn_disabled_when_first_page()

    def check_next_btn_disabled_when_last_page(self):
        return self.pagination.next_btn_disabled_when_last_page()

    def check_is_middle_navigation_work(self):
        return self.pagination.is_middle_navigation_work()
