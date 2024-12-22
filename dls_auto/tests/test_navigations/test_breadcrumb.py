from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.navigations.BreadcrumbPage import BreadcrumbPage
from framework.browser.Browser import Browser


class TestBreadcrumbElement:
    def test_breadcrumb(self):
        main_page = MainPage()
        main_page.open_breadcrumb_page()
        main_page.btn_menu.click()
        breadcrumb_page = BreadcrumbPage()
        Browser.scroll_to_top()
        assert_that(breadcrumb_page.check_is_breadcrumb_not_active(),
                    "Breadcrumb is active when not selected")

        assert_that(breadcrumb_page.check_is_breadcrumb_active(),
                    "Breadcrumb is not active when selected")
