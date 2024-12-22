from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.modals.ModalPage import ModalPage
from framework.browser.Browser import Browser


class TestModalElement:
    def test_modal(self):
        self.open_modal()
        modal_page = ModalPage()
        assert_that(modal_page.check_modal(),
                    "Modal does not have topper and text")

    def test_modal_footer(self):
        self.open_modal()
        modal_page = ModalPage()
        assert_that(modal_page.check_modal_footer(),
                    "Modal with footer does not have footer")

    def test_modal_confirm(self):
        self.open_modal()
        modal_page = ModalPage()
        assert_that(modal_page.check_modal_confirm(),
                    "Confirm modal does not have Ok and Cancel buttons")

    def test_modal_success(self):
        self.open_modal()
        modal_page = ModalPage()
        assert_that(modal_page.check_modal_success(),
                    "Success modal does not have Success icon")

    def test_modal_error(self):
        self.open_modal()
        modal_page = ModalPage()
        assert_that(modal_page.check_modal_error(),
                    "Error modal does not have Error icon")

    def open_modal(self):
        main_page = MainPage()
        main_page.open_modal_page()
        main_page.btn_menu.click()
        Browser.scroll_to_top()