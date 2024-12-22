from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.forms.UploadInputPage import UploadInputPage
from framework.browser.Browser import Browser


class TestUploadInputElement:
    def test_upload_input_element(self):
        main_page = MainPage()
        main_page.open_upload_input_page()
        main_page.btn_menu.click()
        upload_input_page = UploadInputPage()
        Browser.scroll_to_top()
        assert_that(upload_input_page.upload_input_success.is_upload_input_success(),
                    "Success UploadInput does not have success class")
        assert_that(upload_input_page.upload_input_failure.is_upload_input_error(),
                    "Error UploadInput does not have error class")
        assert_that(upload_input_page.upload_input_disabled.is_upload_input_disabled(),
                    "Disabled UploadInput does not have disabled class")
