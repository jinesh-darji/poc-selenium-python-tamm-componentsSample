from dls_auto.elements.notifications.Alert import Alert
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class AlertPage(BasePage):
    page_name = "Alert Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "alert_page_locator")
    alert = Alert(locator_reader, "alert", "btn_close")

    def __init__(self):
        super(AlertPage, self).__init__(self.page_element)

    def check_is_alert_success_exist(self):
        return self.alert.is_alert_success()

    def check_is_alert_info_exist(self):
        return self.alert.is_alert_info()

    def check_is_alert_warning_exist(self):
        return self.alert.is_alert_warning()

    def check_is_alert_error_exist(self):
        return self.alert.is_alert_error()

    def check_is_close_button_work(self):
        return self.alert.is_close_button_closes_alert()
