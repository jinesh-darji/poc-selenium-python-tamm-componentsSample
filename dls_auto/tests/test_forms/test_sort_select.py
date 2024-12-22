from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.forms.SortSelectPage import SortSelectPage
from framework.browser.Browser import Browser


class TestSortSelectElement:
    def test_sort_select_element(self):
        main_page = MainPage()
        main_page.open_sort_select_page()
        main_page.btn_menu.click()
        sort_select_page = SortSelectPage()
        Browser.scroll_to_top()
        assert_that(sort_select_page.check_sort_select_contains_selected_value(),
                    "Sort Select element does not contain selected value")
