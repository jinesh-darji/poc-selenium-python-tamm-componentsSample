from dls_auto.elements.cards.ContactCard import ContactCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ContactCardPage(BasePage):
    page_name = "Contact Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "contact_card_page_locator")
    contact_card = ContactCard(locator_reader, "contact_card", "lbl_title", "lbl_body",
                               "lbl_area", "lbl_phone", "lbl_schedule", "lbl_website", "lbl_map")

    def __init__(self):
        super(ContactCardPage, self).__init__(self.page_element)

    def check_is_card_has_title(self):
        return self.contact_card.is_card_has_title()

    def check_is_card_has_body(self):
        return self.contact_card.is_card_has_body()

    def check_is_card_has_area(self):
        return self.contact_card.is_card_has_area()

    def check_is_card_has_phone(self):
        return self.contact_card.is_card_has_phone()

    def check_is_card_has_schedule(self):
        return self.contact_card.is_card_has_schedule()

    def check_is_card_has_website(self):
        return self.contact_card.is_card_has_website()

    def check_is_card_has_map(self):
        return self.contact_card.is_card_has_map()
