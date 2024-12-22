from dls_auto.elements.swithcers.ContentCheckboxRadioGroup import ContentCheckboxRadioGroup
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ContentCheckboxRadioGroupPage(BasePage):
    page_name = "Content Checkbox Radio Group Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "content_checkbox_radio_group_page_locator")

    chbx_content_checkbox_group = ContentCheckboxRadioGroup(locator_reader, "chbx_content_checkbox_group")
    btn_radio_button_group = ContentCheckboxRadioGroup(locator_reader, "btn_radio_button_group")

    def __init__(self):
        super(ContentCheckboxRadioGroupPage, self).__init__(self.page_element)

    def check_content_checkbox_radio_group_checked(self):
        return self.chbx_content_checkbox_group.is_content_checkbox_group_checked()

    def check_content_checkbox_radio_group_unchecked(self):
        return self.chbx_content_checkbox_group.is_content_checkbox_group_unchecked()

    def check_content_checkbox_radio_group_unchecked_disabled(self):
        return self.chbx_content_checkbox_group.is_content_checkbox_group_unchecked_disabled()

    def check_radio_button_group_checked(self):
        return self.btn_radio_button_group.is_radio_button_group_checked()

    def check_radio_button_group_unchecked(self):
        return self.btn_radio_button_group.is_radio_button_group_unchecked()

    def check_radio_button_group_unchecked_disabled(self):
        return self.btn_radio_button_group.is_radio_button_group_unchecked_disabled()
