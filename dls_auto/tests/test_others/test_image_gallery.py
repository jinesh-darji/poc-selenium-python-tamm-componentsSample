from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.ImageGalleryPage import ImageGalleryPage
from framework.browser.Browser import Browser


class TestImageGalleryElement:
    def test_image_gallery(self):
        main_page = MainPage()
        main_page.open_image_gallery_page()
        main_page.btn_menu.click()
        image_gallery_page = ImageGalleryPage()
        Browser.scroll_to_top()
        assert_that(image_gallery_page.check_is_left_disabled(),
                    "Left Button is not disabled when there are no left elements")
        assert_that(image_gallery_page.check_is_button_active_when_clicked(),
                    "Image Button is not selected when clicked")
        assert_that(image_gallery_page.check_is_right_disabled(),
                    "Right Button is not disabled when there are no right elements")
