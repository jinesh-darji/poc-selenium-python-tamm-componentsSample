# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class NotFound(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_page, lbl_code, lbl_image, btn_back):
        super(NotFound, self).__init__(locator_reader, element_key)
        self.lbl_page = Label(locator_reader, lbl_page)
        self.lbl_code = Label(locator_reader, lbl_code)
        self.lbl_image = Label(locator_reader, lbl_image)
        self.btn_back = Button(locator_reader, btn_back)

    def get_element_type(self):
        return "NotFound"

    def is_page_label_present(self):
        return self.lbl_page.is_present()

    def is_code_label_present(self):
        return self.lbl_code.is_present()

    def is_image_label_present(self):
        return self.lbl_image.is_present()

    def is_btn_back_redirects(self):
        self.btn_back.click()
        return not self.lbl_image.is_present()
