from hamcrest import assert_that

from dls_auto.pages.MainPage import MainPage
from framework.browser.Browser import Browser
from dls_auto.pages.accordions.EventAccordionPage import EventAccordionPage


class TestCollapseElement:

    def test_event_accordion_element_closed_opened(self):
        main_page = MainPage()
        main_page.open_event_accordion_page()
        main_page.btn_menu.click()
        event_accordion_page = EventAccordionPage()
        Browser.scroll_to_top()
        assert_that(event_accordion_page.check_is_accordion_closed(),"Event Accordion element is closed")
        event_accordion_page.get_expansion_accordion()
        assert_that(event_accordion_page.check_is_accordion_opened(), "Event Accordion element is Opened")
