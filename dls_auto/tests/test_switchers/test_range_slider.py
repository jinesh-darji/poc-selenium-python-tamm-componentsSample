from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.RangeSliderPage import RangeSliderPage


class TestRangeSlider:
    def test_range_slider(self):
        main_page = MainPage()
        main_page.open_range_slider_page()

        main_page.btn_menu.click()

        range_slider_page = RangeSliderPage()
        range_slider_page.scroll_to_element(range_slider_page.based_component)

        self.check_sliders(range_slider_page, range_slider_page.sliders_white_color)
        self.check_sliders(range_slider_page, range_slider_page.sliders_black_color)

        list_1 = self.check_clackable_slider(range_slider_page, range_slider_page.sliders_white_color_value,
                                             range_slider_page.slider_1_white, 0)
        assert_that(list_1[0] != list_1[1], "Values are equaled")

        list_2 = self.check_clackable_slider(range_slider_page, range_slider_page.sliders_white_color_value,
                                             range_slider_page.slider_2_white, 4)
        assert_that(list_2[0] != list_2[1], "Values are equaled")

    def check_sliders(self, page_locator, slider_locator):
        assert_that(page_locator.check_slider_2_points_available(slider_locator), "Slider with 2 points isn't "
                                                                                  "available for clicking")
        assert_that(page_locator.check_slider_2_points_disabled(slider_locator), "Slider with 2 points isn't disabled")

        assert_that(page_locator.check_slider_1_point_available(slider_locator), "Slider with 1 point isn't available "
                                                                                 "for clicking")
        assert_that(page_locator.check_slider_1_point_disabled(slider_locator), "Slider with 1 point isn't disabled")

    def check_clackable_slider(self, page_locator, value_locator, slider_locator, index):
        list = []
        value_1 = page_locator.get_slider_value(value_locator, index)
        value_2 = page_locator.click_on_slider(slider_locator, 10, value_locator, index)
        list.append(value_1)
        list.append(value_2)
        return list
