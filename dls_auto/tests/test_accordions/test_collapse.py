from hamcrest import assert_that

from dls_auto.pages.accordions.CollapsePage import CollapsePage
from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser


class TestCollapseElement:

    def test_transparent_collapse_element_closed_opened(self):
        main_page = MainPage()
        main_page.open_collapse_page()
        main_page.btn_menu.click()
        collapse_page = CollapsePage()
        Browser.scroll_to_top()
        assert_that(collapse_page.check_is_accordion_transparent_closed(),"Transparent Accordion element is closed")
        collapse_page.btn_plus_minus_transparent.scroll_by_script()
        collapse_page.get_transparent_expansion_accordion()
        assert_that(collapse_page.check_is_accordion_transparent_opened(), "Transparent Accordion element is Opened")


    def test_opaque_collapse_element_closed_opened(self):
        main_page = MainPage()
        main_page.open_collapse_page()
        main_page.btn_menu.click()
        collapse_page = CollapsePage()
        Browser.scroll_to_top()
        assert_that(collapse_page.check_is_accordion_opaque_closed(),"Opaque Accordion element is closed")
        collapse_page.get_opaque_expansion_accordion()
        assert_that(collapse_page.check_is_accordion_opaque_opened(), "Opaque Accordion element is Opened")
