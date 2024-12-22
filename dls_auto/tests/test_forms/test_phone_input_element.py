from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.forms.PhoneInputPage import PhoneInputPage
from framework.browser.Browser import Browser


class TestPhoneInputElement:
    def test_phone_input_element(self):
        main_page = MainPage()
        main_page.open_phone_input_page()
        main_page.btn_menu.click()
        phone_input_page = PhoneInputPage()
        Browser.scroll_to_top()
        assert_that(phone_input_page.is_phone_input_code_error(), "Phone Input code error is not reflected")
        assert_that(phone_input_page.is_phone_input_code_phone_failure(),
                    "Phone Input code and phone error is not reflected")
        assert_that(phone_input_page.is_phone_input_phone_error(), "Phone Input phone error is not reflected")
        assert_that(phone_input_page.is_phone_input_disabled(), "Phone Input disable is not reflected")
