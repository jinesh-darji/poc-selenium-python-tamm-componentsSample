# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class ProgressBar(BaseElement):
    def __init__(self, locator_reader, element_key):
        super(ProgressBar, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "ProgressBar"

    def is_progress_bar_25_percent(self):
        return "width: 25%" in self.get_elements()[0].get_attribute("style")

    def is_progress_bar_50_percent(self):
        return "width: 50%" in self.get_elements()[1].get_attribute("style")

    def is_progress_bar_100_percent(self):
        return "width: 100%" in self.get_elements()[2].get_attribute("style")

    def is_progress_bar_75_percent(self):
        return "width: 75%" in self.get_elements()[3].get_attribute("style")
