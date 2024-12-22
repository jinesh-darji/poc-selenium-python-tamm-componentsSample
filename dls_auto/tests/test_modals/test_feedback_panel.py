from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.modals.FeedbackPanelPage import FeedbackPanelPage
from framework.browser.Browser import Browser


class TestFeedbackPanelElement:
    def test_feedback_panel_after_selecting_yes(self):
        main_page = MainPage()
        main_page.open_feedback_panel_page()
        main_page.btn_menu.click()
        feedback_panel_page = FeedbackPanelPage()
        Browser.scroll_to_top()
        assert_that(feedback_panel_page.check_thanks_displayed_after_yes(),
                    "Thanks element is not displayed after selecting Yes")

    def test_feedback_panel_after_selecting_no(self):
        main_page = MainPage()
        main_page.open_feedback_panel_page()
        main_page.btn_menu.click()
        feedback_panel_page = FeedbackPanelPage()
        Browser.scroll_to_top()
        assert_that(feedback_panel_page.check_thanks_not_displayed_after_no(),
                    "Thanks element is displayed after selecting No")

    def test_feedback_panel_after_selecting_no_filling_data(self):
        main_page = MainPage()
        main_page.open_feedback_panel_page()
        main_page.btn_menu.click()
        feedback_panel_page = FeedbackPanelPage()
        Browser.scroll_to_top()
        assert_that(feedback_panel_page.check_thanks_displayed_after_filling_email_comment(),
                    "Thanks element is not displayed after selecting No and filling email and comment")