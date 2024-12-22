from dls_auto.elements.forms.TelephoneInput import TelephoneInput
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class PhoneInputPage(BasePage):
    page_name = "Phone Input Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "phone_input_page_locator")
    phone_input_success = TelephoneInput(locator_reader, "phone_input_success", "code_success", "phone_success")
    phone_input_code_failure = TelephoneInput(locator_reader, "phone_input_code_failure", "code_failure",
                                              "phone_success")
    phone_input_phone_failure = TelephoneInput(locator_reader, "phone_input_phone_failure", "code_success",
                                               "phone_failure")
    phone_input_phone_code_failure = TelephoneInput(locator_reader, "phone_input_phone_code_failure", "code_failure",
                                                    "phone_failure")
    phone_input_disabled = TelephoneInput(locator_reader, "phone_input_disabled", "code_success", "phone_success")

    def __init__(self):
        super(PhoneInputPage, self).__init__(self.page_element)

    def is_phone_input_disabled(self):
        return self.phone_input_disabled.is_telephone_input_disabled()

    def is_phone_input_code_error(self):
        return self.phone_input_code_failure.is_telephone_input_code_failure()

    def is_phone_input_phone_error(self):
        return self.phone_input_phone_failure.is_telephone_input_phone_failure()

    def is_phone_input_code_phone_failure(self):
        return self.phone_input_phone_code_failure.is_telephone_input_phone_code_failure()