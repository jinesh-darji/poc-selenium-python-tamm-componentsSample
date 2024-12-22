# coding=utf-8
from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class Alert(BaseElement):
    def __init__(self, locator_reader, element_key, btn_close):
        super(Alert, self).__init__(locator_reader, element_key)
        self.btn_close = Button(locator_reader, btn_close)

    def get_element_type(self):
        return "Alert"

    def is_alert_info(self):
        return "alert_info" in self.get_elements()[0].get_attribute("class")

    def is_alert_success(self):
        return "alert_success" in self.get_elements()[1].get_attribute("class")

    def is_alert_warning(self):
        return "alert_warning" in self.get_elements()[2].get_attribute("class")

    def is_alert_error(self):
        return "alert_error" in self.get_elements()[3].get_attribute("class")

    def is_close_button_closes_alert(self):
        elements_count = self.get_elements_count()
        self.btn_close.wait_until_location_stable()
        self.btn_close.click()
        elements_count_after_close = self.get_elements_count()
        return elements_count - elements_count_after_close == 1

