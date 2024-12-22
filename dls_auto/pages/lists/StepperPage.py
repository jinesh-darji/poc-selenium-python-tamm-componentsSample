from dls_auto.elements.lists.Stepper import Stepper
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class StepperPage(BasePage):
    page_name = "Stepper Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "stepper_page_locator")
    stepper = Stepper(locator_reader, "stepper", "step_complete", "step_in_progress", "step_postponed")

    def __init__(self):
        super(StepperPage, self).__init__(self.page_element)

    def check_is_step_complete_exist(self):
        return self.stepper.is_step_complete_exist()

    def check_is_step_in_progress_exist(self):
        return self.stepper.is_step_in_progress_exist()

    def check_is_step_postponed_exist(self):
        return self.stepper.is_step_postponed_exist()