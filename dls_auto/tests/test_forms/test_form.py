from hamcrest import assert_that

from dls_auto.pages.forms.ButtonDropdownPage import ButtonDropdownPage
from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser
from dls_auto.pages.forms.FormPage import FormPage


class TestForm:
    def test_form_input(self):
        main_page = MainPage()
        main_page.open_form_page()
        main_page.btn_menu.click()
        form_page = FormPage()
        Browser.scroll_to_top()
        assert_that(form_page.check_input_success_has_class(), "Form input doesn't have success view")
        assert_that(form_page.check_input_failure_has_class(), "Form input doesn't have error view")
        assert_that(form_page.check_input_disabled_has_class(), "Form input doesn't have disabled view")
        assert_that(form_page.check_set_input_value(), "Form input doesn't have input set")

        assert_that(form_page.check_textarea_success_has_class(), "Form textarea doesn't have success view")
        assert_that(form_page.check_textarea_failure_has_class(), "Form textarea doesn't have error view")
        assert_that(form_page.check_textarea_disabled_has_class(), "Form textarea doesn't have disabled view")
        assert_that(form_page.check_set_textarea_value(), "Form textarea doesn't have input set")
