from dls_auto.elements.cards.LocationCard import LocationCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class LocationCardPage(BasePage):
    page_name = "Location Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "location_card_page_locator")
    event_card = LocationCard(locator_reader, "location_card", "lbl_hero_title", "lbl_title", "lbl_body",
                              "lbl_image", "lbl_price", "btn_label")

    def __init__(self):
        super(LocationCardPage, self).__init__(self.page_element)

    def check_is_card_has_title(self):
        return self.event_card.is_card_has_title()

    def check_is_card_has_hero_title(self):
        return self.event_card.is_card_has_hero_title()

    def check_is_card_has_body(self):
        return self.event_card.is_card_has_body()

    def check_is_card_has_image(self):
        return self.event_card.is_card_has_image()

    def check_is_card_has_price(self):
        return self.event_card.is_card_has_price()

    def check_is_card_has_btn_label(self):
        return self.event_card.is_card_has_btn_label()
