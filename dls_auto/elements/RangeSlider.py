# coding=utf-8
from framework.elements.base.BaseElement import BaseElement


class RangeSlider(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(RangeSlider, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "RangeSlider"

    def is_slider_2_points_available(self):
        return "ant-slider qa-slider" in self.get_elements()[0].get_attribute("class")

    def is_slider_2_points_disabled(self):
        return "ant-slider-disabled" in self.get_elements()[1].get_attribute("class")

    def is_slider_1_point_available(self):
        return "ant-slider qa-slider" in self.get_elements()[2].get_attribute("class")

    def is_slider_1_point_disabled(self):
        return "ant-slider-disabled" in self.get_elements()[3].get_attribute("class")