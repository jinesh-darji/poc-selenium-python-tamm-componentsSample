from dls_auto.elements.cards.AppointmentCard import AppointmentCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class AppointmentCardPage(BasePage):
    page_name = "Appointment Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "appointment_card_page_locator")
    appointment_card = AppointmentCard(locator_reader, "appointment_card", "lbl_header_content", "lbl_body_header",
                                       "btn_change")

    def __init__(self):
        super(AppointmentCardPage, self).__init__(self.page_element)

    def check_is_card_has_header_content(self):
        return self.appointment_card.is_card_has_header_content()

    def check_is_card_has_body_header(self):
        return self.appointment_card.is_card_has_body_header()

    def check_is_card_has_btn_change(self):
        return self.appointment_card.is_card_has_btn_change()
