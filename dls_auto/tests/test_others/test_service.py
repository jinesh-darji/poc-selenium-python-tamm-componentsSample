from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.ServicePage import ServicePage
from framework.browser.Browser import Browser


class TestServiceElement:
    def test_service(self):
        main_page = MainPage()
        main_page.open_service_page()
        main_page.btn_menu.click()
        service_page = ServicePage()
        Browser.scroll_to_top()
        assert_that(service_page.check_is_image_label_present(),
                    "Image is not present for not found service")
        assert_that(service_page.check_is_title_label_present(),
                    "Title is not present for not found service")
        assert_that(service_page.check_is_subtitle_label_present(),
                    "Subtitle is not present for not found service")
        assert_that(service_page.check_is_btn_back_work(),
                    "Back Button does not work for not found service")
