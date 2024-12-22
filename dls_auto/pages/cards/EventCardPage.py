from dls_auto.elements.cards.EventCard import EventCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class EventCardPage(BasePage):
    page_name = "Event Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "event_card_page_locator")
    event_card = EventCard(locator_reader, "event_card", "lbl_title", "lbl_body",
                           "lbl_image", "lbl_date", "btn_learn_more")

    def __init__(self):
        super(EventCardPage, self).__init__(self.page_element)

    def check_is_card_has_title(self):
        return self.event_card.is_card_has_title()

    def check_is_card_has_body(self):
        return self.event_card.is_card_has_body()

    def check_is_card_has_image(self):
        return self.event_card.is_card_has_image()

    def check_is_card_has_date(self):
        return self.event_card.is_card_has_date()

    def check_is_card_has_btn_learn_more(self):
        return self.event_card.is_card_has_btn_learn_more()
