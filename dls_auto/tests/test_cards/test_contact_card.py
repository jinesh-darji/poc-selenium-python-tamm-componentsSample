from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.ContactCardPage import ContactCardPage
from framework.browser.Browser import Browser


class TestContactCardElement:
    def test_contact_card_element(self):
        main_page = MainPage()
        main_page.open_contact_card_page()
        main_page.btn_menu.click()
        contact_card_page = ContactCardPage()
        Browser.scroll_to_top()
        assert_that(contact_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(contact_card_page.check_is_card_has_body(), "Card does not have body")
        assert_that(contact_card_page.check_is_card_has_area(), "Card does not have area")
        assert_that(contact_card_page.check_is_card_has_phone(), "Card does not have phone")
        assert_that(contact_card_page.check_is_card_has_schedule(), "Card does not have schedule")
        assert_that(contact_card_page.check_is_card_has_website(), "Card does not have website")
