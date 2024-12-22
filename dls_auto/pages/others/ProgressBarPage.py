from dls_auto.elements.others.ProgressBar import ProgressBar
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ProgressBarPage(BasePage):
    page_name = "Progress Bar Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "progress_bar_page_locator")
    progress_bar = ProgressBar(locator_reader, "progress_bar")

    def __init__(self):
        super(ProgressBarPage, self).__init__(self.page_element)
