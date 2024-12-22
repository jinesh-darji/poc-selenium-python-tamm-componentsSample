from hamcrest import assert_that
from dls_auto.pages.buttons.IconButtonPage import IconButtonPage
from dls_auto.pages.MainPage import MainPage


class TestIconButtonElement:
    def test_icon_button_element(self):
        main_page = MainPage()
        main_page.open_icon_button_page()
        main_page.btn_menu.click()
        icon_button_page = IconButtonPage()
        assert_that(icon_button_page.check_icon_button_exists(), "Icon Button does not have Icon class")
        assert_that(icon_button_page.check_icon_button_is_disabled(),
                    "Icon Button does not have disabled class if it is disabled")
        assert_that(icon_button_page.check_icon_button_is_primary(),
                    "Icon Button does not have primary class if it is primary")
