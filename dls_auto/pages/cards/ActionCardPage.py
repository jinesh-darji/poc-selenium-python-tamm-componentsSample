from dls_auto.elements.cards.ActionCard import ActionCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ActionCardPage(BasePage):
    page_name = "Action Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "action_card_page_locator")
    action_card = ActionCard(locator_reader, "action_card", "lbl_header_action", "lbl_header_content",
                             "lbl_body_description", "btn_start_now")

    def __init__(self):
        super(ActionCardPage, self).__init__(self.page_element)

    def check_is_card_has_header_action(self):
        return self.action_card.is_card_has_header_action()

    def check_is_card_has_header_content(self):
        return self.action_card.is_card_has_header_content()

    def check_is_card_has_body_description(self):
        return self.action_card.is_card_has_body_description()

    def check_is_card_has_button(self):
        return self.action_card.is_card_has_btn_start_now()


