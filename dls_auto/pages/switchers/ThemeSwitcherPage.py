from dls_auto.elements.swithcers.ThemeSwitcher import ThemeSwitcher
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ThemeSwitcherPage(BasePage):
    page_name = "Theme Switcher Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "theme_switcher_page_locator")

    btn_dark_black_color = ThemeSwitcher(locator_reader, "btn_dark_black_color")
    btn_light_black_color = ThemeSwitcher(locator_reader, "btn_light_black_color")
    btn_dark_white_color = ThemeSwitcher(locator_reader, "btn_dark_white_color")
    btn_light_white_color = ThemeSwitcher(locator_reader, "btn_light_white_color")

    def __init__(self):
        super(ThemeSwitcherPage, self).__init__(self.page_element)

    def check_dark_btn_black_color(self, btn_locator):
        return btn_locator.is_dark_btn_checked()

    def check_light_btn_black_color(self, btn_locator):
        btn_locator.click_js()
        return btn_locator.is_light_btn_checked()

    def check_dark_btn_white_color(self, btn_locator):
        btn_locator.click_js()
        return btn_locator.is_dark_btn_checked()

    def check_light_btn_white_color(self, btn_locator):
        return btn_locator.is_light_btn_checked()
