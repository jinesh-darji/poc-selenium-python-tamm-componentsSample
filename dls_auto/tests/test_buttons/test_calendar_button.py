from hamcrest import assert_that
from dls_auto.pages.buttons.CalendarButtonPage import CalendarButtonPage
from dls_auto.pages.MainPage import MainPage


class TestCalendarButtonElement:
    def test_calendar_button_element(self):
        main_page = MainPage()
        main_page.open_calendar_button_page()
        main_page.btn_menu.click()
        calendar_button_page = CalendarButtonPage()
        assert_that(calendar_button_page.check_calendar_button_exists(), "Calendar Button does not have calendar class")
        assert_that(calendar_button_page.check_calendar_button_collapsed(),
                    "Calendar Button is not collapsed when clicked")
