from hamcrest import assert_that
from dls_auto.pages.buttons.DownloadButtonPage import DownloadButtonPage
from dls_auto.pages.MainPage import MainPage


class TestDownloadButtonElement:
    def test_download_button_element(self):
        main_page = MainPage()
        main_page.open_download_button_page()
        main_page.btn_menu.click()
        download_button_page = DownloadButtonPage()
        assert_that(download_button_page.check_download_button_exists(), "Download Button does not have download class")
        assert_that(download_button_page.check_button_is_disabled(),
                    "Download Button does not have disabled class when disabled")
