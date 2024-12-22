from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.BadgePage import BadgePage
from framework.browser.Browser import Browser


class TestBadgeElement:
    def test_badge(self):
        main_page = MainPage()
        main_page.open_badge_page()
        main_page.btn_menu.click()
        badge_page = BadgePage()
        Browser.scroll_to_top()
        assert_that(badge_page.check_is_badge_count(),
                    "Badge count does not have count class")
        assert_that(badge_page.check_is_badge_multiple(),
                    "Badge multiple does not have count class")
        assert_that(badge_page.check_is_badge_info_present(),
                    "Info Badge is not present")
