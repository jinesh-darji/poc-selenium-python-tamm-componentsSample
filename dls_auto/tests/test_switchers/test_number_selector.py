from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.NumberSelectorPage import NumberSelectorPage
from framework.browser.Browser import Browser


class TestNumberSelector:
    def test_content_radio_button(self):
        main_page = MainPage()
        main_page.open_number_selector_page()

        main_page.btn_menu.click()

        Browser.scroll_to_top()
        number_selector_page = NumberSelectorPage()

        value_increase = number_selector_page.check_number_selector_available(number_selector_page.
                                                                              btn_number_selector_plus)
        assert_that(int(value_increase[1]) - 1 == int(value_increase[0]), "Number selector isn't increased")

        value_decrease = number_selector_page.check_number_selector_available(number_selector_page.
                                                                              btn_number_selector_minus)
        assert_that(int(value_decrease[0]) - 1 == int(value_decrease[1]), "Number selector isn't increased")
        assert_that(number_selector_page.check_number_selector_plus_disabled(), "Number selector plus isn't disabled")
        assert_that(number_selector_page.check_number_selector_minus_disabled(), "Number selector minus isn't disabled")
        assert_that(int(number_selector_page.lbl_disabled_number_selector_value.get_text()) == 0,
                    "Number selector minus is disabled")