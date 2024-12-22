from framework.elements.base.BaseElement import BaseElement


class ViewAllButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(ViewAllButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "ViewAllButton"

    def is_button_download(self):
        return "uil-view-all-button" in self.get_attribute("class")
