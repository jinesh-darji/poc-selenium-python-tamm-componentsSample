from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.AppointmentCardPage import AppointmentCardPage
from framework.browser.Browser import Browser


class TestAppointmentCardElement:
    def test_appointment_card_element(self):
        main_page = MainPage()
        main_page.open_appointment_card_page()
        main_page.btn_menu.click()
        appointment_card_page = AppointmentCardPage()
        Browser.scroll_to_top()
        assert_that(appointment_card_page.check_is_card_has_header_content(), "Card does not have header content")
        assert_that(appointment_card_page.check_is_card_has_body_header(), "Card does not have body header")
        assert_that(appointment_card_page.check_is_card_has_btn_change(), "Card does not have change button")