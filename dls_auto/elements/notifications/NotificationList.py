# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class NotificationList(BaseElement):
    ELEMENTS_COUNT = 3

    def __init__(self, locator_reader, element_key, icon, btn_explore_all):
        super(NotificationList, self).__init__(locator_reader, element_key)
        self.icon = Label(locator_reader, icon)
        self.btn_explore_all = Button(locator_reader, btn_explore_all)

    def get_element_type(self):
        return "NotificationList"

    def is_notification_has_icon(self):
        return self.icon.get_elements_count() == self.ELEMENTS_COUNT

    def is_notification_has_explore_more_button(self):
        return self.btn_explore_all.get_elements_count() == self.ELEMENTS_COUNT

    def is_notification_list_exist(self):
        return self.is_present()
