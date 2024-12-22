from dls_auto.elements.notifications.NotificationList import NotificationList
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class NotificationListPage(BasePage):
    page_name = "Notification List Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "notification_list_page_locator")
    notification_list = NotificationList(locator_reader, "notification_list", "icon", "btn_explore_all")

    def __init__(self):
        super(NotificationListPage, self).__init__(self.page_element)

    def check_is_notification_list_present(self):
        return self.notification_list.is_notification_list_exist()

    def check_is_notification_icon_in_list(self):
        return self.notification_list.is_notification_has_icon()

    def check_is_notification_button_in_list(self):
        return self.notification_list.is_notification_has_explore_more_button()
