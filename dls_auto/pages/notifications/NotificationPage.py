from dls_auto.elements.notifications.Notification import Notification
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class NotificationPage(BasePage):
    page_name = "Notification Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "notification_page_locator")
    notification = Notification(locator_reader, "notification", "icon")

    def __init__(self):
        super(NotificationPage, self).__init__(self.page_element)

    def check_is_notification_date(self):
        return self.notification.is_notification_date()

    def check_is_notification_icon(self):
        return self.notification.is_notification_icon()

    def check_is_notification_custom(self):
        return self.notification.is_notification_custom()
