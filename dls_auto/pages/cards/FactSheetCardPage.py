from dls_auto.elements.cards.FactSheetCard import FactSheetCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class FactSheetCardPage(BasePage):
    page_name = "Fact Sheet Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "fact_sheet_card_page_locator")
    fact_sheet_card = FactSheetCard(locator_reader, "fact_sheet_card", "lbl_title", "lbl_body",
                                    "lbl_image", "btn_arrow")

    def __init__(self):
        super(FactSheetCardPage, self).__init__(self.page_element)

    def check_is_card_has_title(self):
        return self.fact_sheet_card.is_card_has_title()

    def check_is_card_has_body(self):
        return self.fact_sheet_card.is_card_has_body()

    def check_is_card_has_image(self):
        return self.fact_sheet_card.is_card_has_image()

    def check_is_card_has_btn_arrow(self):
        return self.fact_sheet_card.is_card_has_btn_arrow()
