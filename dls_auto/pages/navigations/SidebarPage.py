from dls_auto.elements.navigations.Footer import Footer
from framework.elements.Label import Label
from framework.elements.List import List
from framework.elements.Button import Button
from dls_auto.elements.buttons.ViewAllButton import ViewAllButton
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SidebarPage(BasePage):
    page_name = "Sidebar Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "sidebar_page_locator")
    start_now = Button(locator_reader,"start_now_btn")
    twitter = Button(locator_reader,"twitter_btn")
    facebook = Button(locator_reader,"facebook_btn")
    email = Button(locator_reader,"email_btn")
    related_content = List(locator_reader,"related_content_list")
    related_journeys = List(locator_reader,"related_journeys_list")
    view_all_journeys = ViewAllButton(locator_reader,"view_all_journeys_btn")
    view_all_services = ViewAllButton(locator_reader,"view_all_services_btn")


    def __init__(self):
        super(SidebarPage, self).__init__(self.page_element)

    def check_is_start_now_primary(self):
        return self.start_now.is_button_primary()

    def check_is_twitter_btn_present(self):
        return self.twitter.is_present()

    def check_is_facebook_btn_present(self):
        return self.facebook.is_present()

    def check_is_email_btn_present(self):
        return self.email.is_present()

    def check_is_related_content_list_present(self):
        return self.related_content.is_present()

    def check_is_related_journey_list_present(self):
        return self.related_journeys.is_present()

    def check_button_is_view_all_journeys(self):
        return self.view_all_journeys.is_button_download()

    def check_button_is_view_all_services(self):
        return self.view_all_services.is_button_download()
