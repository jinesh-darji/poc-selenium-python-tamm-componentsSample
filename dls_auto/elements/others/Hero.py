# coding=utf-8
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class Hero(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_image, lbl_title, lbl_subtitle):
        super(Hero, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_subtitle = Label(locator_reader, lbl_subtitle)
        self.lbl_image = Label(locator_reader, lbl_image)

    def get_element_type(self):
        return "Hero"

    def is_title_label_present(self):
        return self.lbl_title.is_present()

    def is_subtitle_label_present(self):
        return self.lbl_subtitle.is_present()

    def is_image_label_present(self):
        return self.lbl_image.is_present()
