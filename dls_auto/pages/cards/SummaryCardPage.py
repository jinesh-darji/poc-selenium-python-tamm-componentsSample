from dls_auto.elements.cards.SummaryCard import SummaryCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SummaryCardPage(BasePage):
    page_name = "Summary Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "summary_card_page_locator")
    summary_card = SummaryCard(locator_reader, "summary_card", "lbl_title", "lbl_subtitle", "lbl_desc_list", "lbl_desc",
                               "lbl_desc_large")

    def __init__(self):
        super(SummaryCardPage, self).__init__(self.page_element)

    def check_is_card_has_title(self):
        return self.summary_card.is_card_has_title()

    def check_is_card_has_subtitle(self):
        return self.summary_card.is_card_has_subtitle()

    def check_is_card_has_desc_list(self):
        return self.summary_card.is_card_has_desc_list()

    def check_is_card_has_description_title(self):
        return self.summary_card.is_card_has_desc_title()

    def check_is_card_has_desc_summary(self):
        return self.summary_card.is_card_has_desc_summary()
