from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.NotFoundPage import NotFoundPage
from framework.browser.Browser import Browser


class TestTableElement:
    def test_table(self):
        main_page = MainPage()
        main_page.open_not_found_page()
        main_page.btn_menu.click()
        not_found_page = NotFoundPage()
        Browser.scroll_to_top()
        assert_that(not_found_page.check_is_page_label_present(),
                    "Not Found label is not present")
        assert_that(not_found_page.check_is_code_label_present(),
                    "Not Found code is not present")
        assert_that(not_found_page.check_is_image_label_present(),
                    "Not Found Image is not present")
        assert_that(not_found_page.check_is_btn_back_redirects(),
                    "Back Button does not redirect to another page")
