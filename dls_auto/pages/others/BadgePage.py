from dls_auto.elements.others.Badge import Badge
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class BadgePage(BasePage):
    page_name = "Badge Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "badge_page_locator")
    badge_count = Badge(locator_reader, "badge_count")
    badge_multiple = Badge(locator_reader, "badge_multiple")
    badge_info = Badge(locator_reader, "badge_info")

    def __init__(self):
        super(BadgePage, self).__init__(self.page_element)

    def check_is_badge_count(self):
        return self.badge_count.is_badge_count()

    def check_is_badge_multiple(self):
        return self.badge_multiple.is_badge_multiple()

    def check_is_badge_info_present(self):
        return self.badge_info.is_present()