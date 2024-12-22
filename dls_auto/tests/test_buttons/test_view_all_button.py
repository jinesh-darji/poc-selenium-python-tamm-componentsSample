
from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.buttons.ViewAllButtonPage import ViewAllButtonPage
from framework.browser.Browser import Browser


class TestViewAllButtonElement:
    def test_view_all_button_element(self):
        main_page = MainPage()
        main_page.open_view_all_button_page()
        main_page.btn_menu.click()
        view_all_button_page = ViewAllButtonPage()
        Browser.scroll_to_top()
        assert_that(view_all_button_page.check_button_is_view_all(), "View All Button does not have View All class")