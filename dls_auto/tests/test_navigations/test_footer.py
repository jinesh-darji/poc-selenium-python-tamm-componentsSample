from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.navigations.FooterPage import FooterPage
from framework.browser.Browser import Browser


class TestFooterElement:
    def test_footer(self):
        main_page = MainPage()
        main_page.open_footer_page()
        main_page.btn_menu.click()
        footer_page = FooterPage()
        Browser.scroll_to_top()
        assert_that(footer_page.check_is_useful_links_present(),
                    "Useful Links section is not present")

        assert_that(footer_page.check_is_support_present(),
                    "Support section is not present")

        assert_that(footer_page.check_is_follow_us_present(),
                    "Follow us section is not present")

        assert_that(footer_page.check_is_accessibility_present(),
                    "Accessibility section is not present")

        assert_that(footer_page.check_is_btn_language_present(),
                    "Select Language section is not present")