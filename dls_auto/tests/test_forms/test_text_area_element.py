from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.forms.TextAreaPage import TextAreaPage
from framework.browser.Browser import Browser


class TestTextAreaElement:
    def test_text_area_element(self):
        main_page = MainPage()
        main_page.open_text_area_page()
        main_page.btn_menu.click()
        text_area_page = TextAreaPage()
        Browser.scroll_to_top()
        assert_that(text_area_page.text_area_success.is_text_area_success(), "Success TextArea does not have success class")
        assert_that(text_area_page.text_area_failure.is_text_area_error(), "Error TextArea does not have error class")
        assert_that(text_area_page.text_area_disabled.is_text_area_disabled(), "Disabled TextArea does not have disabled class")