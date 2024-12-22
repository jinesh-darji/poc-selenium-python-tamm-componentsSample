# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class ToDoList(BaseElement):
    def __init__(self, locator_reader, element_key, lbl_title, btn_complete, chckbx_complete,
                 btn_arrow):
        super(ToDoList, self).__init__(locator_reader, element_key)
        self.lbl_title = Label(locator_reader, lbl_title)
        self.btn_complete = Button(locator_reader, btn_complete)
        self.chckbx_complete = Button(locator_reader, chckbx_complete)
        self.btn_arrow = Button(locator_reader, btn_arrow)

    def get_element_type(self):
        return "ToDoList"

    def is_title_in_list(self):
        return self.lbl_title.is_present()

    def is_button_arrow_in_list(self):
        return self.btn_arrow.is_present()

    def is_checkbox_checked_when_clicked(self):
        self.btn_complete.click()
        return "checked" in self.chckbx_complete.get_attribute("class")

    def is_checkbox_not_checked_when_not_clicked(self):
        return "checked" not in self.chckbx_complete.get_attribute("class")

