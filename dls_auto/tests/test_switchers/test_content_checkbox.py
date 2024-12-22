from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.ContentCheckboxPage import ContentCheckboxPage
from framework.browser.Browser import Browser


class TestContentCheckbox:
    def test_content_checkbox(self):
        main_page = MainPage()
        main_page.open_content_checkbox_page()

        main_page.btn_menu.click()

        content_checkbox_page = ContentCheckboxPage()
        Browser.scroll_to_top()

        self.check_status_of_checkboxes(content_checkbox_page, content_checkbox_page.chbx_content)

    def check_status_of_checkboxes(self, page_locator, checkbox_locator):
        assert_that(page_locator.check_content_checkbox_checked(checkbox_locator), "Content checkbox doesn't have "
                                                                                   "checked status")
        assert_that(page_locator.check_content_checkbox_checked_disabled(checkbox_locator), "Content checkbox doesn't "
                                                                                            "have checked and "
                                                                                            "disabled status")
        assert_that(page_locator.check_content_checkbox_unchecked(checkbox_locator), "Content checkbox doesn't have "
                                                                                     "unchecked status")
        assert_that(page_locator.check_content_checkbox_disabled(checkbox_locator), "Content checkbox doesn't have "
                                                                                    "disabled status")
