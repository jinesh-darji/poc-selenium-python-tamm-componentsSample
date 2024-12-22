from dls_auto.elements.buttons.IconButton import IconButton
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class IconButtonPage(BasePage):
    page_name = "Icon Button Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "icon_button_page_locator")
    btn_icon_primary = IconButton(locator_reader, "btn_icon_primary")
    btn_icon_primary_disabled = IconButton(locator_reader, "btn_icon_primary_disabled")
    btn_icon = IconButton(locator_reader, "btn_icon")
    btn_icon_disabled = IconButton(locator_reader, "btn_icon_disabled")

    def __init__(self):
        super(IconButtonPage, self).__init__(self.page_element)

    def check_icon_button_exists(self):
        return self.btn_icon.is_button_icon()

    def check_icon_button_is_primary(self):
        return self.btn_icon_primary.is_button_primary()

    def check_icon_button_is_disabled(self):
        return self.btn_icon_disabled.is_button_disabled() and self.btn_icon_primary_disabled.is_button_disabled()
