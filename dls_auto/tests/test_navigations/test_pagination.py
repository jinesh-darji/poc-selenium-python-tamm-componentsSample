from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.navigations.PaginationPage import PaginationPage
from framework.browser.Browser import Browser


class TestPaginationElement:
    def test_pagination(self):
        main_page = MainPage()
        main_page.open_pagination_page()
        main_page.btn_menu.click()
        pagination_page = PaginationPage()
        Browser.scroll_to_top()
        assert_that(pagination_page.check_is_random_page_clicked(),
                    "Random page does not have checked class after clicking")

        assert_that(pagination_page.check_next_btn_disabled_when_last_page(),
                    "Next Button is not disabled when last page is selected")

        assert_that(pagination_page.check_prev_btn_disabled_when_first_page(),
                    "Previous Button is not disabled when first page is selected")

        assert_that(pagination_page.check_is_middle_navigation_work(),
                    "Incorrect page is checked when navigating in the middle")
