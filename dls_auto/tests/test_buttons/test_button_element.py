from hamcrest import assert_that

from dls_auto.pages.buttons.ButtonPage import ButtonPage
from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser


class TestButtonElement:
    def test_button_element(self):
        main_page = MainPage()
        main_page.open_button_page()
        main_page.btn_menu.click()
        button_page = ButtonPage()
        Browser.scroll_to_top()
        # assert_that(button_page.check_btn_default_has_correct_class(), "Default Button has incorrect class")
        # assert_that(button_page.check_btn_primary_has_correct_class(), "Primary Button has incorrect class")
        # assert_that(button_page.check_btn_print_has_correct_class(), "Print Button has incorrect class")
        # assert_that(button_page.check_btn_secondary_has_correct_class(), "Secondary Button has incorrect class")
        # assert_that(button_page.check_btn_text_has_correct_class(), "Text Button has incorrect class")
        # assert_that(button_page.check_btn_text_secondary_has_correct_class(),
        #             "Text Secondary Button has incorrect class")
        # assert_that(button_page.btn_default.is_button_disabled(),
        #             "Default Button does not have disabled attribute")
        # assert_that(button_page.btn_primary.is_button_disabled(),
        #             "Primary Button does not have disabled attribute")
        # assert_that(button_page.btn_print.is_button_disabled(),
        #             "Print Button does not have disabled attribute")
        # assert_that(button_page.btn_secondary.is_button_disabled(),
        #             "Secondary Button does not have disabled attribute")
        # assert_that(button_page.btn_text_secondary.is_button_disabled(),
        #             "Secondary Text Button does not have disabled attribute")
        # assert_that(button_page.btn_text.is_button_disabled(),
        #             "Text Button does not have disabled attribute")
