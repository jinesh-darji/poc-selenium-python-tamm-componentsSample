from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.lists.StepperPage import StepperPage
from dls_auto.pages.modals.FeedbackPanelPage import FeedbackPanelPage
from framework.browser.Browser import Browser


class TestStepperElement:
    def test_stepper(self):
        main_page = MainPage()
        main_page.open_stepper_page()
        main_page.btn_menu.click()
        stepper_page = StepperPage()
        Browser.scroll_to_top()
        assert_that(stepper_page.check_is_step_complete_exist(),
                    "Complete step does not exist")
        assert_that(stepper_page.check_is_step_in_progress_exist(),
                    "In progress step does not exist")
        assert_that(stepper_page.check_is_step_postponed_exist(),
                    "Postponed step does not exist")

