from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.navigations.TabsPage import TabsPage
from framework.browser.Browser import Browser


class TestTabsElement:
    def test_horizontal_tab(self):
        self.start_tabs_test()
        tabs_page = TabsPage()
        assert_that(tabs_page.horizontal_tab.is_tab_not_selected(),
                    "Horizontal tab element has selected attribute when not selected")
        assert_that(tabs_page.horizontal_tab.is_tab_selected(),
                    "Horizontal tab element has no selected attribute when selected")

    def test_vertical_tab(self):
        self.start_tabs_test()
        tabs_page = TabsPage()
        assert_that(tabs_page.vertical_tab.is_tab_not_selected(),
                    "Vertical tab element has selected attribute when not selected")
        assert_that(tabs_page.vertical_tab.is_tab_selected(),
                    "Vertical tab element has no selected attribute when selected")

    def test_horizontal_scroll_tab(self):
        self.start_tabs_test()
        tabs_page = TabsPage()
        assert_that(tabs_page.horizontal_tab_scroll.is_tab_selected(),
                    "Horizontal tab scroll element has no selected attribute when selected")

        assert_that(tabs_page.horizontal_tab_scroll.is_tab_not_selected(),
                    "Horizontal scroll tab element has selected attribute when not selected")

        assert_that(tabs_page.horizontal_tab_scroll.is_scroll_left_disabled(),
                    "Left scroll is not disabled when there are no options available")

        assert_that(tabs_page.horizontal_tab_scroll.is_scroll_right_disabled(),
                    "Right scroll is not disabled when there are no options available")

    def test_vertical_scroll_tab(self):
        self.start_tabs_test()
        tabs_page = TabsPage()
        assert_that(tabs_page.vertical_tab_scroll.is_tab_selected(),
                    "Vertical tab scroll element has no selected attribute when selected")

        assert_that(tabs_page.vertical_tab_scroll.is_tab_not_selected(),
                    "Vertical scroll tab element has selected attribute when not selected")

        assert_that(tabs_page.vertical_tab_scroll.is_scroll_left_disabled(),
                    "Left scroll is not disabled when there are no options available")

        assert_that(tabs_page.vertical_tab_scroll.is_scroll_right_disabled(),
                    "Right scroll is not disabled when there are no options available")

    def start_tabs_test(self):
        main_page = MainPage()
        main_page.open_tabs_page()
        main_page.btn_menu.click()
        Browser.scroll_to_top()
