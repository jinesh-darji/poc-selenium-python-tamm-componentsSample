from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.ProgressBarPage import ProgressBarPage
from framework.browser.Browser import Browser


class TestProgressBarElement:
    def test_progress_bar(self):
        main_page = MainPage()
        main_page.open_progress_bar_page()
        main_page.btn_menu.click()
        progress_bar_page = ProgressBarPage()
        Browser.scroll_to_top()
        assert_that(progress_bar_page.progress_bar.is_progress_bar_25_percent(),
                    "25% progress bar not found")
        assert_that(progress_bar_page.progress_bar.is_progress_bar_50_percent(),
                    "50% progress bar not found")
        assert_that(progress_bar_page.progress_bar.is_progress_bar_100_percent(),
                    "100% progress bar not found")
        assert_that(progress_bar_page.progress_bar.is_progress_bar_75_percent(),
                    "75% progress bar not found")
