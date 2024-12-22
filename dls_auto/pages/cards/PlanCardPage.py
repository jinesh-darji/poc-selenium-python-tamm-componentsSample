from dls_auto.elements.cards.PlanCard import PlanCard
from dls_auto.elements.cards.ProfileCard import ProfileCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class PlanCardPage(BasePage):
    page_name = "Plan Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "plan_card_page_locator")
    plan_card = PlanCard(locator_reader, "plan_card", "btn_plan", "lbl_title", "lbl_body",
                         "btn_apply")

    def __init__(self):
        super(PlanCardPage, self).__init__(self.page_element)

    def check_is_card_has_title(self):
        return self.plan_card.is_card_has_title()

    def check_is_card_has_body(self):
        return self.plan_card.is_card_has_body()

    def check_is_card_has_btn_apply(self):
        return self.plan_card.is_card_has_btn_apply()

    def check_is_card_plan_btn_checked(self):
        return self.plan_card.is_card_plan_btn_checked()
