from selenium.webdriver import ActionChains

from dls_auto.elements.RangeSlider import RangeSlider
from framework.browser.Browser import Browser
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RangeSliderPage(BasePage):
    page_name = "Range Slider Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "range_slider_page_locator")

    based_component = RangeSlider(locator_reader, "based_component")
    sliders_white_color = RangeSlider(locator_reader, "sliders_white_color")
    sliders_black_color = RangeSlider(locator_reader, "sliders_black_color")
    sliders_white_color_value = RangeSlider(locator_reader, "sliders_white_color_value")
    sliders_black_color_value = RangeSlider(locator_reader, "sliders_black_color_value")
    slider_1_white = RangeSlider(locator_reader, "slider_1_white")
    slider_2_white = RangeSlider(locator_reader, "slider_2_white")

    def __init__(self):
        super(RangeSliderPage, self).__init__(self.page_element)

    def check_slider_2_points_available(self, slider_locator):
        return slider_locator.is_slider_2_points_available()

    def check_slider_2_points_disabled(self, slider_locator):
        return slider_locator.is_slider_2_points_disabled()

    def check_slider_1_point_available(self, slider_locator):
        return slider_locator.is_slider_1_point_available()

    def check_slider_1_point_disabled(self, slider_locator):
        return slider_locator.is_slider_1_point_disabled()

    def get_slider_value(self, slider_locator, index):
        value = slider_locator.get_elements_text()[index]
        return value

    def click_on_slider(self, slider_locator, step, value_locator, index):
        Browser.scroll_by_keys()
        en = slider_locator.find_element()
        Browser.scroll_to_top()
        move = ActionChains(Browser.get_driver())
        Browser.wait_for_page_to_load()
        move.click_and_hold(en).move_by_offset(step, 0).release().perform()
        Browser.wait_for_page_to_load()
        return self.get_slider_value(value_locator, index)