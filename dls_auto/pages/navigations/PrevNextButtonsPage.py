from dls_auto.elements.navigations.PrevNextButtons import PrevNextButtons
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class PrevNextButtonsPage(BasePage):
    page_name = "Prev Next Buttons Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "prev_next_buttons_page_locator")
    prev_next_buttons = PrevNextButtons(locator_reader, "prev_next_buttons", "btn_next",
                                        "btn_prev")

    def __init__(self):
        super(PrevNextButtonsPage, self).__init__(self.page_element)

    def check_prev_next_buttons_enabled(self):
        self.prev_next_buttons.btn_next.format('1')
        self.prev_next_buttons.btn_prev.format('1')
        return self.prev_next_buttons.is_next_button_present() and self.prev_next_buttons.is_prev_button_present()

    def check_prev_enabled_next_disabled_buttons(self):
        self.prev_next_buttons.btn_next.format('2')
        self.prev_next_buttons.btn_prev.format('2')
        return self.prev_next_buttons.is_next_button_disabled()

    def check_prev_disabled_next_enabled_buttons(self):
        self.prev_next_buttons.btn_next.format('3')
        self.prev_next_buttons.btn_prev.format('3')
        return self.prev_next_buttons.is_prev_button_disabled()

    def check_prev_disabled_next_disabled_buttons(self):
        self.prev_next_buttons.btn_next.format('4')
        self.prev_next_buttons.btn_prev.format('4')
        return self.prev_next_buttons.is_next_button_disabled() and self.prev_next_buttons.is_prev_button_disabled()

    def check_prev_exists_next_empty_buttons(self):
        self.prev_next_buttons.btn_next.format('5')
        self.prev_next_buttons.btn_prev.format('5')
        return self.prev_next_buttons.is_prev_button_present()

    def check_prev_empty_next_exists_buttons(self):
        self.prev_next_buttons.btn_next.format('6')
        self.prev_next_buttons.btn_prev.format('6')
        return self.prev_next_buttons.is_prev_button_present()
