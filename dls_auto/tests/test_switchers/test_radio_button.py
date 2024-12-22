from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.RadioButtonPage import RadioButtonPage
from framework.browser.Browser import Browser


class TestRadioButton:
    def test_radio_button(self):
        main_page = MainPage()
        main_page.open_radio_button_page()

        main_page.btn_menu.click()

        radio_button_page = RadioButtonPage()
        Browser.scroll_to_top()

        self.check_status_of_radio_buttons(radio_button_page, radio_button_page.btn_radio_button_black_color)
        self.check_status_of_radio_buttons(radio_button_page, radio_button_page.btn_radio_button_white_color)

    def check_status_of_radio_buttons(self, page_locator, radio_button_locator):
        assert_that(page_locator.check_radio_button_unchecked(radio_button_locator), "Radio button doesn't have "
                                                                                     "unchecked status")
        assert_that(page_locator.check_radio_button_checked(radio_button_locator), "Radio button doesn't have checked "
                                                                                   "status")
        assert_that(page_locator.check_radio_button_disabled(radio_button_locator), "Radio button doesn't have disabled"
                                                                                    "status")
        assert_that(page_locator.check_radio_button_checked_disabled(radio_button_locator), "Radio button doesn't have "
                                                                                            "checked and disabled "
                                                                                            "status")
