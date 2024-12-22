# coding=utf-8
from dls_auto.elements.lists.Stepper import Stepper
from framework.elements.Label import Label


class VerticalStepper(Stepper):
    def __init__(self, locator_reader, element_key, step_complete, step_in_progress, step_postponed, lbl_current_step,
                 step_tmplt):
        super(VerticalStepper, self).__init__(locator_reader, element_key, step_complete, step_in_progress,
                                              step_postponed)
        self.lbl_current_step = Label(locator_reader, lbl_current_step)
        self.step_tmplt = Label(locator_reader, step_tmplt)

    def get_element_type(self):
        return "VerticalStepper"

    def is_step_shown_when_selected(self):
        step = self.step_in_progress.get_random_item_from_list()
        self.step_tmplt.format(step)
        self.step_tmplt.click()
        self.lbl_current_step.format(step)
        return self.lbl_current_step.is_present()
