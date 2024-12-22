from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.SpinnerPage import SpinnerPage
from framework.browser.Browser import Browser


class TestSpinnerElement:
    def test_spinner(self):
        main_page = MainPage()
        main_page.open_spinner_page()
        main_page.btn_menu.click()
        spinner_page = SpinnerPage()
        Browser.scroll_to_top()
        assert_that(spinner_page.check_is_default_spinner_inversed(),
                    "Default spinner is not inversed")
        assert_that(spinner_page.check_is_circle_spinner_inversed(),
                    "Circle spinner is not inversed")
        assert_that(spinner_page.check_is_spinner_circle(),
                    "Circle Spinner has no circle class")
