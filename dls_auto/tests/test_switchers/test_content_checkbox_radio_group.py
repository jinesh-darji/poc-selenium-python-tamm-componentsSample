from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.switchers.ContentCheckboxRadioGroupPage import ContentCheckboxRadioGroupPage
from framework.browser.Browser import Browser


class TestContentCheckboxRadioGroup:
    def test_theme_switcher(self):
        main_page = MainPage()
        main_page.open_content_checkbox_radio_group_page()

        main_page.btn_menu.click()

        content_checkbox_radio_group_page = ContentCheckboxRadioGroupPage()
        Browser.scroll_to_top()

        assert_that(content_checkbox_radio_group_page.check_content_checkbox_radio_group_checked(), "Content checkbox "
                                                                                                    "doesn't have "
                                                                                                    "checked status")
        assert_that(content_checkbox_radio_group_page.check_content_checkbox_radio_group_unchecked(), "Content checkbox"
                                                                                                      " doesn't "
                                                                                                      "have checked "
                                                                                                      "status")
        assert_that(content_checkbox_radio_group_page.check_content_checkbox_radio_group_unchecked_disabled(),
                    "Content checkbox doesn't have "
                    "unchecked and disabled status")

        assert_that(content_checkbox_radio_group_page.check_radio_button_group_checked(), "Radio button doesn't have "
                                                                                          "checked status")
        assert_that(content_checkbox_radio_group_page.check_radio_button_group_unchecked(), "Radio button doesn't have "
                                                                                            "unchecked status")
        assert_that(content_checkbox_radio_group_page.check_radio_button_group_unchecked_disabled(), "Radio button "
                                                                                                     "unchecked and "
                                                                                                     "disabled status")
