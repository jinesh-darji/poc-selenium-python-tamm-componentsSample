from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.navigations.PrevNextButtonsPage import PrevNextButtonsPage
from framework.browser.Browser import Browser


class TestPrevNextButtonsElement:
    def test_prev_next_buttons(self):
        main_page = MainPage()
        main_page.open_prev_next_buttons_page()
        main_page.btn_menu.click()
        prev_next_buttons_page = PrevNextButtonsPage()
        Browser.scroll_to_top()
        assert_that(prev_next_buttons_page.check_prev_next_buttons_enabled(),
                    "Prev Next buttons are not enabled on first element")

        assert_that(prev_next_buttons_page.check_prev_enabled_next_disabled_buttons(),
                    "Prev button is not enabled and next button is not disabled on 2nd element")

        assert_that(prev_next_buttons_page.check_prev_disabled_next_enabled_buttons(),
                    "Prev button is not disabled and next button is not enabled on 3rd element")

        assert_that(prev_next_buttons_page.check_prev_disabled_next_disabled_buttons(),
                    "Prev button is not disabled and next button is not enabled on 4th element")

        assert_that(prev_next_buttons_page.check_prev_exists_next_empty_buttons(),
                    "Prev button is not exist and next button is not empty on 5th element")

        assert_that(prev_next_buttons_page.check_prev_exists_next_empty_buttons(),
                    "Prev button is not empty and next button is not exist on 6th element")