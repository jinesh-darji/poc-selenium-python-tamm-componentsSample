from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.navigations.SidebarPage import SidebarPage
from framework.browser.Browser import Browser


class TestSidebar:
    def test_sidebar(self):
        main_page = MainPage()
        main_page.open_sidebar_page()
        main_page.btn_menu.click()
        sidebar_page = SidebarPage()
        Browser.scroll_to_top()
        assert_that(sidebar_page.check_is_start_now_primary(),
                    "Start now button is primary")

        assert_that(sidebar_page.check_is_related_content_list_present(),
                    "Related Content list is present")

        assert_that(sidebar_page.check_is_related_journey_list_present(),
                    "Related Journeys list is present")

        assert_that(sidebar_page.check_is_twitter_btn_present(),
                    "Twitter button is present")

        assert_that(sidebar_page.check_is_facebook_btn_present(),
                    "Facebook button is present")

        assert_that(sidebar_page.check_is_email_btn_present(),
                    "Email button is present")

        assert_that(sidebar_page.check_button_is_view_all_journeys(),
                    "View  all journeys button is present")

        assert_that(sidebar_page.check_button_is_view_all_services(),
                    "TView  all services button is present")
