from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.buttons.SocialShareButtonPage import SocialShareButtonPage
from framework.browser.Browser import Browser


class TestSocialShareButtonElement:
    def test_social_share_button_element(self):
        main_page = MainPage()
        main_page.open_social_share_button_page()
        main_page.btn_menu.click()
        social_share_button_page = SocialShareButtonPage()
        Browser.scroll_to_top()
        assert_that(social_share_button_page.check_social_share_button_exists(),
                    "Social SHare button does not have social share class")
        assert_that(social_share_button_page.check_social_share_button_is_disabled(),
                    "Social Share button does not have disabled class when disabled")

