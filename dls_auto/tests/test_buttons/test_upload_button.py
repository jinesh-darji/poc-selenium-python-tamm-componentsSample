from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.buttons.UploadButtonPage import UploadButtonPage
from framework.browser.Browser import Browser


class TestUploadButtonElement:
    def test_upload_button_element(self):
        main_page = MainPage()
        main_page.open_upload_button_page()
        main_page.btn_menu.click()
        upload_button_page = UploadButtonPage()
        Browser.scroll_to_top()
        assert_that(upload_button_page.check_upload_button_is_present(), "Upload button is not present")
        assert_that(upload_button_page.check_upload_button_is_disabled(), "Upload button does not have disabled class")