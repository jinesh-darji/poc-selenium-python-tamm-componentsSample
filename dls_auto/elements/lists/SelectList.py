# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class SelectList(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_title, lbl_item_title, lbl_item_description, btn_complete,
                 chckbx_complete):
        super(SelectList, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.lbl_item_title = Label(locator_reader, lbl_item_title)
        self.lbl_item_description = Label(locator_reader, lbl_item_description)
        self.btn_complete = Button(locator_reader, btn_complete)
        self.chckbx_complete = Button(locator_reader, chckbx_complete)

    def get_element_type(self):
        return "SelectList"

    def is_title_in_list(self):
        return self.lbl_title.is_present()

    def is_item_title_in_list(self):
        return self.lbl_item_title.is_present()

    def is_item_description_in_list(self):
        return self.lbl_item_description.is_present()

    def is_checkbox_checked_when_clicked(self):
        self.btn_complete.click()
        return "uil-icon-check" in self.btn_complete.get_attribute("class")

    def is_checkbox_single_select(self):
        self.btn_complete.get_elements()[0].click()
        self.btn_complete.get_elements()[1].click()
        return "uil-icon-check" not in self.btn_complete.get_elements()[0].get_attribute("class")

