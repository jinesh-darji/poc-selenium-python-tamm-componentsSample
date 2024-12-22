from dls_auto.elements.cards.CompareCard import CompareCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CompareCardPage(BasePage):
    page_name = "Compare Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "compare_card_page_locator")
    compare_card = CompareCard(locator_reader, "compare_card", "lbl_title", "lbl_body",
                               "lbl_criteria", "btn_compare", "chkbx_compare")

    def __init__(self):
        super(CompareCardPage, self).__init__(self.page_element)

    def check_is_card_has_title(self):
        return self.compare_card.is_card_has_title()

    def check_is_card_has_body(self):
        return self.compare_card.is_card_has_body()

    def check_is_card_has_criteria(self):
        return self.compare_card.is_card_has_criteria()

    def check_is_card_has_btn_compare(self):
        return self.compare_card.is_card_has_btn_compare()

    def check_is_compare_button_checked(self):
        return self.compare_card.is_compare_button_checked()
