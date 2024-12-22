from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.TagPage import TagPage
from framework.browser.Browser import Browser


class TestTagElement:
    def test_tag(self):
        main_page = MainPage()
        main_page.open_tag_page()
        main_page.btn_menu.click()
        tag_page = TagPage()
        Browser.scroll_to_top()
        assert_that(tag_page.check_is_tag_closed(),
                    "Tag is not closed")
