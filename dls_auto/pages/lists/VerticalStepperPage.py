from dls_auto.elements.lists.VerticalStepper import VerticalStepper
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class VerticalStepperPage(BasePage):
    page_name = "Vertical Stepper Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "vertical_stepper_page_locator")
    vertical_stepper = VerticalStepper(locator_reader, "vertical_stepper", "step_complete", "step_in_progress", "step_postponed", "lbl_current_step", "step_tmplt")

    def __init__(self):
        super(VerticalStepperPage, self).__init__(self.page_element)

    def check_is_step_complete_exist(self):
        return self.vertical_stepper.is_step_complete_exist()

    def check_is_step_in_progress_exist(self):
        return self.vertical_stepper.is_step_in_progress_exist()

    def check_is_step_postponed_exist(self):
        return self.vertical_stepper.is_step_postponed_exist()

    def check_is_step_shown_when_selected(self):
        return self.vertical_stepper.is_step_shown_when_selected()