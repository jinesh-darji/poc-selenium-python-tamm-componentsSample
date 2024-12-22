from dls_auto.elements.cards.SmallDescriptionCard import SmallDescriptionCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SmallDescriptionCardPage(BasePage):
    page_name = "Small Description Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "small_description_card_page_locator")
    small_description_card = SmallDescriptionCard(locator_reader, "small_description_card", "lbl_title",
                                                  "lbl_body_desc", "btn_learn_more")

    def __init__(self):
        super(SmallDescriptionCardPage, self).__init__(self.page_element)

    def check_is_card_has_title(self):
        return self.small_description_card.is_card_has_title()

    def check_is_card_has_body_desc(self):
        return self.small_description_card.is_card_has_body_desc()

    def check_is_card_has_btn_learn_more(self):
        return self.small_description_card.is_card_has_btn_learn_more()
