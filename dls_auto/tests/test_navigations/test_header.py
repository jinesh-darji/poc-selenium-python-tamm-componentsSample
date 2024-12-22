from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.navigations.HeaderPage import HeaderPage
from framework.browser.Browser import Browser


class TestHeaderElement:
    def test_header(self):
        main_page = MainPage()
        main_page.open_header_page()
        main_page.btn_menu.click()
        header_page = HeaderPage()
        Browser.scroll_to_top()
        assert_that(header_page.check_is_btn_menu_present(),
                    "Side Menu button is not present")

        assert_that(header_page.check_is_lbl_logo_present(),
                    "Logo is not present")

        assert_that(header_page.check_is_btn_language_present(),
                    "Change Language button is not present")

        assert_that(header_page.check_is_btn_search_present(),
                    "Search button is not present")

        assert_that(header_page.check_is_btn_feedback_present(),
                    "Feedback Button is not present")

        assert_that(header_page.check_is_side_menu_opened(), "Side menu is not opened after clicking Menu button")
        assert_that(header_page.check_is_feedback_slide_opened(),
                    "Feedback Slide menu is not opened after clicking Feedback button")
