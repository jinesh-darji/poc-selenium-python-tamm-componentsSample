

from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.CarouselPage import CarouselPage
from framework.browser.Browser import Browser


class TestCarouselElement:
    def test_carousel(self):
        main_page = MainPage()
        main_page.open_carousel_page()
        main_page.btn_menu.click()
        carousel_page = CarouselPage()
        Browser.scroll_to_top()
        assert_that(carousel_page.check_is_image_change_when_click_hor(),
                    "Image does not change when clicking horizontal carousel")
        assert_that(carousel_page.check_is_image_change_when_click_vert(),
                    "Image does not change when clicking vertical carousel")
