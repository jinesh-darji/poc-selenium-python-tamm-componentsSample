from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.lists.CompositeListPage import CompositeListPage
from framework.browser.Browser import Browser


class TestCompositeListElement:
    def test_composite_list_heading_element(self):
        self.open_composite_list()
        composite_list_page = CompositeListPage()
        assert_that(composite_list_page.list_heading.is_title_in_list(), "Heading List does not have title")
        assert_that(composite_list_page.list_heading.is_description_in_list(), "Heading List does not have description")
        assert_that(composite_list_page.list_heading.is_button_arrow_in_list(),
                    "Heading List does not have button arrow")
        assert_that(composite_list_page.list_heading.is_checkbox_not_checked_when_not_clicked(),
                    "Checkbox is checked when not clicked")
        assert_that(composite_list_page.list_heading.is_checkbox_checked_when_clicked(),
                    "Heading List checkbox is not checked when clicked")

    def test_composite_list_todo_element(self):
        self.open_composite_list()
        composite_list_page = CompositeListPage()
        assert_that(composite_list_page.to_do_list.is_title_in_list(), "Heading List does not have title")
        assert_that(composite_list_page.to_do_list.is_title_in_list(), "Heading List does not have title")
        assert_that(composite_list_page.to_do_list.is_button_arrow_in_list(),
                    "Heading List does not have button arrow")
        assert_that(composite_list_page.to_do_list.is_checkbox_not_checked_when_not_clicked(),
                    "Checkbox is checked when not clicked ")
        assert_that(composite_list_page.list_heading.is_checkbox_checked_when_clicked(),
                    "Checkbox is not checked when clicked")

    def test_multi_select_list_todo_element(self):
        self.open_composite_list()
        composite_list_page = CompositeListPage()
        assert_that(composite_list_page.multi_select_list.is_title_in_list(), "MultiSelect List does not have title")
        assert_that(composite_list_page.multi_select_list.is_item_title_in_list(),
                    "MultiSelect List does not have item title")
        assert_that(composite_list_page.multi_select_list.is_item_description_in_list(),
                    "MultiSelect List does not have item title")
        assert_that(composite_list_page.multi_select_list.is_checkbox_checked_when_clicked(),
                    "Checkbox is not checked when clicked")

    def test_single_select_list_todo_element(self):
        self.open_composite_list()
        composite_list_page = CompositeListPage()
        assert_that(composite_list_page.single_select_list.is_title_in_list(), "MultiSelect List does not have title")
        assert_that(composite_list_page.single_select_list.is_item_title_in_list(),
                    "MultiSelect List does not have item title")
        assert_that(composite_list_page.single_select_list.is_item_description_in_list(),
                    "MultiSelect List does not have item title")
        assert_that(composite_list_page.single_select_list.is_checkbox_checked_when_clicked(),
                    "Checkbox is not checked when clicked")
        assert_that(composite_list_page.single_select_list.is_checkbox_single_select(),
                    "Multiple checkboxes can be checked")

    def open_composite_list(self):
        main_page = MainPage()
        main_page.open_composite_list_page()
        main_page.btn_menu.click()
        Browser.scroll_to_top()
