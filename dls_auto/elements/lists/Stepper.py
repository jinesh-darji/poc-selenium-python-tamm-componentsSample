# coding=utf-8
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class Stepper(BaseElement):
    def __init__(self, locator_reader, element_key, step_complete, step_in_progress, step_postponed):
        super(Stepper, self).__init__(locator_reader, element_key)
        self.step_complete = Label(locator_reader, step_complete)
        self.step_in_progress = Label(locator_reader, step_in_progress)
        self.step_postponed = Label(locator_reader, step_postponed)


    def get_element_type(self):
        return "Stepper"

    def is_step_complete_exist(self):
        return self.step_complete.is_present()

    def is_step_in_progress_exist(self):
        return self.step_complete.is_present()

    def is_step_postponed_exist(self):
        return self.step_complete.is_present()
