from hamcrest import assert_that
from dls_auto.pages.forms.InputPage import InputPage
from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser


class TestInputElement:
    def test_input_element(self):
        main_page = MainPage()
        main_page.open_input_page()
        main_page.btn_menu.click()
        input_page = InputPage()
        Browser.scroll_to_top()
        assert_that(input_page.input_failure.is_text_box_failure(), "Failure Textbox does not have error class")
        assert_that(input_page.input_success.is_text_box_success(), "Success Textbox does not have success class")
        assert_that(input_page.input_disabled.is_text_box_disabled(), "Disabled Textbox does not have disabled class")