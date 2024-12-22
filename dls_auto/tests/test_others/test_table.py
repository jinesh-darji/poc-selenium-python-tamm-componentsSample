from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.TablePage import TablePage
from framework.browser.Browser import Browser


class TestTableElement:
    def test_table(self):
        main_page = MainPage()
        main_page.open_table_page()
        main_page.btn_menu.click()
        table_page = TablePage()
        Browser.scroll_to_top()
        assert_that(table_page.check_is_all_chxkbx_checked(),
                    "Checkboxes are not checked when All checkbox is clicked")
        assert_that(table_page.check_is_all_chxkbx_unchecked(),
                    "Checkboxes are not unchecked when All checkbox is clicked")
        assert_that(table_page.check_is_enabled_checked(),
                    "Checkbox is not checked when clicked")
        assert_that(table_page.check_is_disabled_not_checked(),
                    "Disabled Checkbox is checked when clicked")
