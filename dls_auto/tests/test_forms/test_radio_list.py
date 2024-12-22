from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.forms.RadioListPage import RadioListPage
from framework.browser.Browser import Browser


class TestRadioList:
    def test_radio_list(self):
        main_page = MainPage()
        main_page.open_radio_list_page()
        main_page.btn_menu.click()
        radio_list_page = RadioListPage()
        Browser.scroll_to_top()
        assert_that(radio_list_page.check_radio_button_is_unchecked(), "Check Button is not unchecked by default")
        assert_that(radio_list_page.check_radio_button_is_checked(), "Check Button is not checked after clicking")