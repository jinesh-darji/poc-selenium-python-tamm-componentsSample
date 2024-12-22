# coding=utf-8
import random

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class Carousel(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_title, btn_carousel):
        super(Carousel, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.btn_carousel = Button(locator_reader, btn_carousel)

    def get_element_type(self):
        return "Carousel"

    def is_title_label_present(self):
        self.get_text()
        return self.lbl_title.is_present()


    def is_image_change_when_click(self):
        index = random.randint(0, self.btn_carousel.get_elements_count() - 1)
        self.btn_carousel.wait_until_location_stable()
        self.btn_carousel.get_elements()[index].click()
        self.lbl_title.wait_until_location_stable()
        return str(index + 1) in self.lbl_title.get_text()
