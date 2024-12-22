from dls_auto.elements.cards.Card import Card
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CardPage(BasePage):
    page_name = "Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "card_page_locator")
    card = Card(locator_reader, "card", "lbl_image", "lbl_title",
                "lbl_body", "btn_view")

    def __init__(self):
        super(CardPage, self).__init__(self.page_element)

    def check_is_card_has_image(self):
        return self.card.is_card_has_image()

    def check_is_card_has_title(self):
        return self.card.is_card_has_title()

    def check_is_card_has_body(self):
        return self.card.is_card_has_body()

    def check_is_card_has_btn_view(self):
        return self.card.is_card_has_btn_view()
