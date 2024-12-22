from dls_auto.elements.cards.SmallCard import SmallCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SmallCardPage(BasePage):
    page_name = "Small Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "small_card_page_locator")
    small_card = SmallCard(locator_reader, "small_card", "lbl_card_name", "lbl_card_desc", "btn_learn_more")

    def __init__(self):
        super(SmallCardPage, self).__init__(self.page_element)

    def check_is_card_has_card_name(self):
        return self.small_card.is_card_has_card_name()

    def check_is_card_has_card_desc(self):
        return self.small_card.is_card_has_card_desc()

    def check_is_card_has_btn_learn_more(self):
        return self.small_card.is_card_has_btn_learn_more()



