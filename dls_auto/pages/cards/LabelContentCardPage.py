from dls_auto.elements.cards.LabelContentCard import LabelContentCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class LabelContentCardPage(BasePage):
    page_name = "Label Content Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "label_content_card_page_locator")
    label_content_card = LabelContentCard(locator_reader, "label_content_card", "lbl_title", "lbl_body")

    def __init__(self):
        super(LabelContentCardPage, self).__init__(self.page_element)

    def check_is_card_has_title(self):
        return self.label_content_card.is_card_has_title()

    def check_is_card_has_body(self):
        return self.label_content_card.is_card_has_body()
