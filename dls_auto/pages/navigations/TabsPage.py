from dls_auto.elements.navigations.Tab import Tab
from dls_auto.elements.navigations.TabScroll import TabScroll
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TabsPage(BasePage):
    page_name = "Tabs Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "tabs_page_locator")
    horizontal_tab = Tab(locator_reader, "horizontal_tab")
    vertical_tab = Tab(locator_reader, "vertical_tab")
    horizontal_tab_scroll = TabScroll(locator_reader, "horizontal_tab_scroll", "btn_scroll_left_hor",
                                      "btn_scroll_right_hor")
    vertical_tab_scroll = TabScroll(locator_reader, "vertical_tab_scroll", "btn_scroll_up_vert",
                                    "btn_scroll_down_vert")

    def __init__(self):
        super(TabsPage, self).__init__(self.page_element)
