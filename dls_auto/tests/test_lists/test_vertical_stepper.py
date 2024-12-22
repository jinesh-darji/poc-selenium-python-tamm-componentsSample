from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.lists.VerticalStepperPage import VerticalStepperPage
from framework.browser.Browser import Browser


class TestVerticalStepperElement:
    def test_stepper(self):
        main_page = MainPage()
        main_page.open_vertical_stepper_page()
        main_page.btn_menu.click()
        vertical_stepper_page = VerticalStepperPage()
        Browser.scroll_to_top()
        assert_that(vertical_stepper_page.check_is_step_complete_exist(),
                    "Complete step does not exist")
        assert_that(vertical_stepper_page.check_is_step_in_progress_exist(),
                    "In progress step does not exist")
        assert_that(vertical_stepper_page.check_is_step_postponed_exist(),
                    "Postponed step does not exist")
        assert_that(vertical_stepper_page.check_is_step_shown_when_selected(),
                    "Step Info is not shown when selected")

