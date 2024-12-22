from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.SwitchPage import SwitchPage
from framework.browser.Browser import Browser


class TestSwitch:
    def test_switch(self):
        main_page = MainPage()
        main_page.open_switch_button_page()

        main_page.btn_menu.click()

        switch_page = SwitchPage()
        Browser.scroll_to_top()

        assert_that(switch_page.check_switch_button_unchecked(), "Switch button doesn't have unchecked status")
        assert_that(switch_page.check_switch_button_checked(), "Switch button doesn't have checked status")
        assert_that(switch_page.check_switch_button_unchecked_disabled(), "Switch button doesn't have unchecked and "
                                                                          "disabled status")
        assert_that(switch_page.check_switch_button_checked_disabled(), "Switch button doesn't have checked and "
                                                                        "disabled status")

        assert_that(switch_page.check_status_switch_button_changed(switch_page.btn_switch_unchecked,
                                                                   switch_page.check_switch_button_checked()),
                    "Status doesn't changed to checked")

        assert_that(switch_page.check_status_switch_button_changed(switch_page.btn_switch_checked,
                                                                   switch_page.check_switch_button_unchecked()),
                    "Status doesn't changed to unchecked")
