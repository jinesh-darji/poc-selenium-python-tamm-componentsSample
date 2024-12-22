from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.ThemeSwitcherPage import ThemeSwitcherPage
from framework.browser.Browser import Browser


class TestThemeSwitcher:
    def test_theme_switcher(self):
        main_page = MainPage()
        main_page.open_theme_switcher_page()

        main_page.btn_menu.click()

        theme_switcher_page = ThemeSwitcherPage()
        Browser.scroll_to_top()

        assert_that(theme_switcher_page.check_dark_btn_black_color(theme_switcher_page.btn_dark_black_color),
                    "Dark button isn't selected")
        assert_that(theme_switcher_page.check_light_btn_black_color(theme_switcher_page.btn_light_black_color),
                    "Dark button isn't selected")
        assert_that(theme_switcher_page.check_light_btn_white_color(theme_switcher_page.btn_light_white_color),
                    "Dark button isn't selected")
        assert_that(theme_switcher_page.check_dark_btn_white_color(theme_switcher_page.btn_dark_white_color),
                    "Dark button isn't selected")