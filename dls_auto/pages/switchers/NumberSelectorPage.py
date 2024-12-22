from dls_auto.elements.swithcers.NumberSelector import NumberSelector
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class NumberSelectorPage(BasePage):
    page_name = "Number Selector Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "number_selector_page_locator")

    btn_number_selector_minus = NumberSelector(locator_reader, "btn_number_selector_minus")
    btn_number_selector_plus = NumberSelector(locator_reader, "btn_number_selector_plus")
    btn_disabled_number_selector_minus = NumberSelector(locator_reader, "btn_disabled_number_selector_minus")
    btn_disabled_number_selector_plus = NumberSelector(locator_reader, "btn_disabled_number_selector_plus")
    lbl_number_selector_value = Label(locator_reader, "number_selector_value")
    lbl_disabled_number_selector_value = Label(locator_reader, "disabled_number_selector_value")

    def __init__(self):
        super(NumberSelectorPage, self).__init__(self.page_element)

    def check_number_selector_available(self, selector_locator):
        value_list = []
        default_value = self.lbl_number_selector_value.get_text()
        value_list.append(default_value)
        selector_locator.click_number_selector()
        new_value = self.lbl_number_selector_value.get_text()
        value_list.append(new_value)
        return value_list

    def check_number_selector_minus_disabled(self):
        return self.btn_disabled_number_selector_minus.is_number_selector_minus_disabled()

    def check_number_selector_plus_disabled(self):
        return self.btn_disabled_number_selector_plus.is_number_selector_plus_disabled()
