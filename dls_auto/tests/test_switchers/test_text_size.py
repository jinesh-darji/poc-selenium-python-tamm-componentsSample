from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.TextSizePage import TextSizePage
from framework.browser.Browser import Browser


class TestTextSize:
    def test_text_size(self):
        main_page = MainPage()
        main_page.open_text_size_page()

        main_page.btn_menu.click()

        text_size_page = TextSizePage()
        Browser.scroll_to_top()

        # Clickable, highlight check impossible in DLS site without some functionalities connected with these buttons

        assert_that(text_size_page.is_increase_btn_black_color_present(), "Button isn't present")
        assert_that(text_size_page.is_decrease_btn_black_color_present(), "Button isn't present")
        assert_that(text_size_page.is_increase_btn_white_color_present(), "Button isn't present")
        assert_that(text_size_page.is_decrease_btn_white_color_present(), "Button isn't present")