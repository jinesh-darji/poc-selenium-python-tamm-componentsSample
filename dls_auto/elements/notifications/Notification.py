# coding=utf-8
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.base.BaseElement import BaseElement


class Notification(BaseElement):
    ELEMENTS_COUNT = 3
    
    def __init__(self, locator_reader, element_key, icon):
        super(Notification, self).__init__(locator_reader, element_key)
        self.icon = Label(locator_reader, icon)

    def get_element_type(self):
        return "Notification"

    def is_notification_date(self):
        return self.icon.get_elements_count() == self.ELEMENTS_COUNT-1

    def is_notification_icon(self):
        return "uil-icon-error_outline" in self.icon.get_elements()[0].get_attribute("class")

    def is_notification_custom(self):
        return "uil-icon-error_warning" in self.icon.get_elements()[1].get_attribute("class")

