from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.NavLinkPage import NavLinkPage
from framework.browser.Browser import Browser


class TestNavLinkElement:
    def test_nav_link(self):
        main_page = MainPage()
        main_page.open_nav_link_page()
        main_page.btn_menu.click()
        nav_link_page = NavLinkPage()
        Browser.scroll_to_top()
        assert_that(nav_link_page.check_is_btn_back_work(),
                    "Back Button does not work")
        assert_that(nav_link_page.check_is_btn_forward_work(),
                    "Forward Button does not work")
        assert_that(nav_link_page.check_is_btn_page_work(),
                    "Page Button does not work")
