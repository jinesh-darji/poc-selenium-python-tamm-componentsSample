from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.forms.SearchInputPage import SearchInputPage
from framework.browser.Browser import Browser


class TestSearchInput:
    def test_search_input_element(self):
        main_page = MainPage()
        main_page.open_search_input_page()
        main_page.btn_menu.click()
        search_input_page = SearchInputPage()
        Browser.scroll_to_top()
        assert_that(search_input_page.check_is_possible_to_send_keys(), "Not possible to send keys to Search Input")