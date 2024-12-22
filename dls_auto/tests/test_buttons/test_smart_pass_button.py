from hamcrest import assert_that

from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.buttons.SmartPassButtonPage import SmartPassButtonPage
from framework.browser.Browser import Browser


class TestTLoadMoreButtonElement:
    def test_load_more_button_element(self):
        main_page = MainPage()
        main_page.open_smart_pass_button_page()
        main_page.btn_menu.click()
        smart_pass_button_page = SmartPassButtonPage()
        Browser.scroll_to_top()
        assert_that(smart_pass_button_page.check_smart_pass_button_is_large(), "Success Select does not have success class")
        assert_that(smart_pass_button_page.check_smart_pass_button_is_disabled(), "Error Select does not have error class")