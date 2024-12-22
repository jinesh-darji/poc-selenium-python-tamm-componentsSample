from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.forms.SelectPage import SelectPage
from framework.browser.Browser import Browser


class TestSelectElement:
    def test_select_element(self):
        main_page = MainPage()
        main_page.open_select_page()
        main_page.btn_menu.click()
        select_page = SelectPage()
        Browser.scroll_to_top()
        assert_that(select_page.select_success.is_select_success(), "Success Select does not have success class")
        assert_that(select_page.select_failure.is_select_error(), "Error Select does not have error class")
        assert_that(select_page.select_disabled.is_select_disabled(), "Disabled Select does not have disabled class")