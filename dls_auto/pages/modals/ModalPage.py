from dls_auto.elements.modals.Modal import Modal
from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ModalPage(BasePage):
    page_name = "Modal Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "modal_page_locator")
    modal = Modal(locator_reader, "modal", "lbl_footer", "lbl_topper", "lbl_text", "btn_next", "lbl_success",
                  "lbl_error", "btn_ok", "btn_cancel")
    btn_modal = Button(locator_reader, "btn_modal")
    btn_modal_footer = Button(locator_reader, "btn_modal_footer")
    btn_modal_confirm = Button(locator_reader, "btn_modal_confirm")
    btn_modal_success = Button(locator_reader, "btn_modal_success")
    btn_modal_error = Button(locator_reader, "btn_modal_error")

    def __init__(self):
        super(ModalPage, self).__init__(self.page_element)

    def check_modal(self):
        self.btn_modal.wait_until_location_stable()
        self.btn_modal.click()
        return self.modal.is_modal_has_topper() and self.modal.is_modal_has_text()

    def check_modal_footer(self):
        self.btn_modal_footer.wait_until_location_stable()
        self.btn_modal_footer.click()
        return self.modal.is_modal_has_footer() and self.modal.is_modal_has_text() and self.modal.is_modal_has_topper()

    def check_modal_confirm(self):
        self.btn_modal_confirm.wait_until_location_stable()
        self.btn_modal_confirm.click()
        return self.modal.is_modal_has_topper() and self.modal.is_modal_has_text() and self.modal.is_modal_confirm()

    def check_modal_success(self):
        self.btn_modal_success.wait_until_location_stable()
        self.btn_modal_success.click()
        return self.modal.is_modal_has_text() and self.modal.is_modal_has_success() \
            and self.modal.is_modal_has_button()

    def check_modal_error(self):
        self.btn_modal_error.wait_until_location_stable()
        self.btn_modal_error.click()
        return self.modal.is_modal_has_text() and self.modal.is_modal_has_error() \
            and self.modal.is_modal_has_button()
