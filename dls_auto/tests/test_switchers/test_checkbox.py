from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.CheckboxPage import CheckboxPage
from framework.browser.Browser import Browser


class TestCheckbox:
    def test_checkbox(self):
        main_page = MainPage()
        main_page.open_checkbox_page()

        main_page.btn_menu.click()

        checkbox_page = CheckboxPage()
        Browser.scroll_to_top()

        self.check_status_of_checkboxes(checkbox_page, checkbox_page.chbx_black_color)
        self.check_status_of_checkboxes(checkbox_page, checkbox_page.chbx_white_color)

    def check_status_of_checkboxes(self, page_locator, checkbox_locator):
        assert_that(page_locator.check_checkbox_unchecked(checkbox_locator), "Checkbox doesn't have unchecked status")
        assert_that(page_locator.check_checkbox_checked(checkbox_locator), "Checkbox doesn't have checked status")
        assert_that(page_locator.check_checkbox_disabled(checkbox_locator), "Checkbox doesn't have disabled status")
        assert_that(page_locator.check_checkbox_checked_disabled(checkbox_locator), "Checkbox doesn't have checked and "
                                                                                    "disabled status")
