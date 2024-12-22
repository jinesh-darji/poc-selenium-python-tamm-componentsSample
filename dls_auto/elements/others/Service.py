# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class Service(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_image, lbl_title, lbl_subtitle, btn_back):
        super(Service, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_subtitle = Label(locator_reader, lbl_subtitle)
        self.lbl_image = Label(locator_reader, lbl_image)
        self.btn_back = Button(locator_reader, btn_back)

    def get_element_type(self):
        return "Service"

    def is_title_label_present(self):
        return self.lbl_title.is_present()

    def is_subtitle_label_present(self):
        return self.lbl_subtitle.is_present()

    def is_image_label_present(self):
        return self.lbl_image.is_present()

    def is_btn_back_work(self):
        self.btn_back.click()
        return not self.btn_back.is_present()
