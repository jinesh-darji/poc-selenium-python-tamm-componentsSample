from dls_auto.elements.forms.ButtonDropdown import ButtonDropdown
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ButtonDropdownPage(BasePage):
    page_name = "Button Dropdown Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "button_dropdown_page_locator")
    btn_dropdown = ButtonDropdown(locator_reader, "btn_dropdown")
    btn_dropdown_icon = ButtonDropdown(locator_reader, "btn_dropdown_icon")

    def __init__(self):
        super(ButtonDropdownPage, self).__init__(self.page_element)

    def check_btn_dropdown_is_opened(self):
        return self.btn_dropdown_icon.is_button_dropdown_opened()

    def check_btn_dropdown_is_closed(self):
        return self.btn_dropdown_icon.is_button_dropdown_closed()
