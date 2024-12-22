import time

from dls_auto.elements.others.Service import Service
from dls_auto.elements.others.Spinner import Spinner
from dls_auto.elements.others.ToolTip import Tooltip
from framework.browser.Browser import Browser
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TooltipPage(BasePage):
    page_name = "Tooltip Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "tooltip_page_locator")
    tooltip = Tooltip(locator_reader, "tooltip")

    def __init__(self):
        super(TooltipPage, self).__init__(self.page_element)

    def check_is_tooltip_shown_when_hover(self):
        self.tooltip.move_to_element()
        time.sleep(3)

        self.tooltip.move_to_element()
        return self.tooltip.is_tooltip_shown()

    def check_is_tooltip_not_shown_when_not_hover(self):
        return not self.tooltip.is_tooltip_shown()