from framework.elements.base.BaseElement import BaseElement


class IconButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(IconButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "IconButton"

    def is_button_primary(self):
        return "uil-icon-button_primary" in self.get_attribute("class")

    def is_button_icon(self):
        return "uil-icon-button" in self.get_attribute("class")

    def is_button_disabled(self):
        return "disabled" in self.get_attribute("class")

