from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.PlanCardPage import PlanCardPage
from framework.browser.Browser import Browser


class TestPlanCardElement:
    def test_plan_card_element(self):
        main_page = MainPage()
        main_page.open_plan_card_page()
        main_page.btn_menu.click()
        plan_card_page = PlanCardPage()
        Browser.scroll_to_top()
        assert_that(plan_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(plan_card_page.check_is_card_has_body(), "Card does not have body")
        assert_that(plan_card_page.check_is_card_has_btn_apply(), "Card does not have apply button")
        assert_that(plan_card_page.check_is_card_plan_btn_checked(), "Checkbox is not checked when clicked")
