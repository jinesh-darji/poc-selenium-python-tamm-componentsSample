from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.buttons.ToggleButtonPage import ToggleButtonPage
from framework.browser.Browser import Browser


class TestToggleButtonElement:
    def test_toggle_button_element(self):
        main_page = MainPage()
        main_page.open_toggle_button_page()
        main_page.btn_menu.click()
        toggle_button_page = ToggleButtonPage()
        Browser.scroll_to_top()
        assert_that(toggle_button_page.check_toggle_button_is_toggled(), "Success Select does not have success class")
        assert_that(toggle_button_page.check_toggle_button_is_untoggled(), "Error Select does not have error class")
        assert_that(toggle_button_page.check_toggle_button_is_disabled(), "Disabled Select does not have disabled class")