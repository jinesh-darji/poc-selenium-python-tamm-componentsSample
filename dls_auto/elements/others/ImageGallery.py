# coding=utf-8
from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class ImageGallery(BaseElement):
    def __init__(self, locator_reader, element_key, btn_left, btn_right, btn_image, lbl_selected_image):
        super(ImageGallery, self).__init__(locator_reader, element_key)
        self.btn_left = Button(locator_reader, btn_left)
        self.btn_right = Button(locator_reader, btn_right)
        self.btn_image = Button(locator_reader, btn_image)
        self.lbl_selected_image = Button(locator_reader, lbl_selected_image)

    def get_element_type(self):
        return "ImageGallery"

    def is_button_active(self):
        return "selected" in self.btn_image.get_attribute("class")

    def is_left_disabled(self):
        return "right-nav" in self.btn_left.get_attribute("class")

    def is_right_disabled(self):
        return "left-nav" in self.btn_right.get_attribute("class")