# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class PlanCard(BaseElement):
    def __init__(self, locator_reader, element_key, btn_plan, lbl_title, lbl_body, btn_apply):
        super(PlanCard, self).__init__(locator_reader, element_key)
        self.btn_plan = Button(locator_reader, btn_plan)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_body = Label(locator_reader, lbl_body)
        self.btn_apply = Button(locator_reader, btn_apply)

    def get_element_type(self):
        return "PlanCard"

    def is_card_has_title(self):
        return self.lbl_title.is_present()

    def is_card_plan_btn_checked(self):
        self.btn_plan.click()
        return "icon-check" in self.btn_plan.get_attribute("class")

    def is_card_has_body(self):
        return self.lbl_body.is_present()

    def is_card_has_btn_apply(self):
        return self.btn_apply.is_present()
