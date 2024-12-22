from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.ContentRadioButtonPage import ContentRadioButtonPage
from framework.browser.Browser import Browser


class TestContentRadioButton:
    def test_content_radio_button(self):
        main_page = MainPage()
        main_page.open_content_radio_button_page()

        main_page.btn_menu.click()

        content_radio_button_page = ContentRadioButtonPage()
        Browser.scroll_to_top()

        assert_that(content_radio_button_page.check_content_radio_button_checked(), "Radio button doesn't have checked "
                                                                                    "status")
        assert_that(content_radio_button_page.check_content_radio_button_unchecked(), "Radio button doesn't have "
                                                                                      "unchecked status")
        assert_that(content_radio_button_page.check_content_radio_button_unchecked_disabled(), "Radio button doesn't "
                                                                                               "have unchecked and "
                                                                                               "disabled status")
        assert_that(content_radio_button_page.check_content_radio_button_checked_disabled(), "Radio button doesn't have"
                                                                                             "checked and disabled "
                                                                                             "status")
