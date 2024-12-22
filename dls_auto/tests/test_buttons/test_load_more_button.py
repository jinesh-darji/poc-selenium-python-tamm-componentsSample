from hamcrest import assert_that
from dls_auto.pages.buttons.LoadMoreButtonPage import LoadMoreButtonPage
from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser


class TestTLoadMoreButtonElement:
    def test_load_more_button_element(self):
        main_page = MainPage()
        main_page.open_load_more_button_page()
        main_page.btn_menu.click()
        load_bore_button_page = LoadMoreButtonPage()
        Browser.scroll_to_top()
        assert_that(load_bore_button_page.check_load_more_button_is_active(), "Success Select does not have success class")
        assert_that(load_bore_button_page.check_load_more_button_is_loading(), "Error Select does not have error class")
        assert_that(load_bore_button_page.check_load_more_button_is_disabled(), "Disabled Select does not have disabled class")