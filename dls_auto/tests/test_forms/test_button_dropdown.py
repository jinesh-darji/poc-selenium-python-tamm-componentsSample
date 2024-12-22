from hamcrest import assert_that

from dls_auto.pages.forms.ButtonDropdownPage import ButtonDropdownPage
from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser


class TestButtonDropdownElement:
    def test_button_dropdown_element(self):
        main_page = MainPage()
        main_page.open_button_dropdown_page()
        main_page.btn_menu.click()
        button_dropdown_page = ButtonDropdownPage()
        Browser.scroll_to_top()
        assert_that(button_dropdown_page.check_btn_dropdown_is_closed(), "dropdown Button is not closed by default")
        button_dropdown_page.btn_dropdown.wait_until_location_stable()
        button_dropdown_page.btn_dropdown.click()
        assert_that(button_dropdown_page.check_btn_dropdown_is_opened(), "Dropdown Button is not opened after click")
