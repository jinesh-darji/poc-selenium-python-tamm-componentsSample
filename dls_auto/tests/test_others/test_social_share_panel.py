from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.SocialSharePanelPage import SocialSharePanelPage
from framework.browser.Browser import Browser


class TestSocialSharePanelElement:
    def test_social_share_panel(self):
        main_page = MainPage()
        main_page.open_social_share_panel_page()
        main_page.btn_menu.click()
        social_share_panel_page = SocialSharePanelPage()
        Browser.scroll_to_top()
        assert_that(social_share_panel_page.social_share_panel.is_btn_apple_present(),
                    "Apple Button is not displayed")
        assert_that(social_share_panel_page.social_share_panel.is_btn_envelope_present(),
                    "Envelope Button is not displayed")
        assert_that(social_share_panel_page.social_share_panel.is_btn_envelope_0_present(),
                    "Envelope White Button is not displayed")
        assert_that(social_share_panel_page.social_share_panel.is_btn_facebook_present(),
                    "Facebook Button is not displayed")
        assert_that(social_share_panel_page.social_share_panel.is_btn_google_present(),
                    "Google Button is not displayed")
        assert_that(social_share_panel_page.social_share_panel.is_btn_more_present(),
                    "More Button is not displayed")

        assert_that(social_share_panel_page.social_share_panel.is_btn_apple_disabled(),
                    "Apple Button is not disabled")
        assert_that(social_share_panel_page.social_share_panel.is_btn_envelope_disabled(),
                    "Envelope Button is not disabled")
        assert_that(social_share_panel_page.social_share_panel.is_btn_envelope_0_disabled(),
                    "Envelope White Button is not disabled")
        assert_that(social_share_panel_page.social_share_panel.is_btn_facebook_disabled(),
                    "Facebook Button is not disabled")
        assert_that(social_share_panel_page.social_share_panel.is_btn_google_disabled(),
                    "Google Button is not disabled")
        assert_that(social_share_panel_page.social_share_panel.is_btn_more_disabled(),
                    "More Button is not disabled")