from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TextSizePage(BasePage):
    page_name = "Text Size Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "text_size_page_locator")

    btn_increase_black_color = Button(locator_reader, "btn_increase_black_color")
    btn_decrease_black_color = Button(locator_reader, "btn_decrease_black_color")
    btn_increase_white_color = Button(locator_reader, "btn_increase_white_color")
    btn_decrease_white_color = Button(locator_reader, "btn_decrease_white_color")

    def __init__(self):
        super(TextSizePage, self).__init__(self.page_element)

    def is_increase_btn_black_color_present(self):
        return self.btn_increase_black_color.is_present()

    def is_decrease_btn_black_color_present(self):
        return self.btn_decrease_black_color.is_present()

    def is_increase_btn_white_color_present(self):
        return self.btn_increase_white_color.is_present()

    def is_decrease_btn_white_color_present(self):
        return self.btn_decrease_white_color.is_present()