from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.others.HeroPage import HeroPage
from framework.browser.Browser import Browser


class TestHeroElement:
    def test_hero(self):
        main_page = MainPage()
        main_page.open_hero_page()
        main_page.btn_menu.click()
        hero_page = HeroPage()
        Browser.scroll_to_top()
        assert_that(hero_page.check_is_image_label_present_i(),
                    "Image is not present for hero with image")
        assert_that(hero_page.check_is_image_label_not_present(),
                    "Image is present for hero without image")
        assert_that(hero_page.check_is_title_label_present_i(),
                    "Title is not present for hero with image")
        assert_that(hero_page.check_is_title_label_present(),
                    "Title is not present for hero without image")
        assert_that(hero_page.check_is_subtitle_label_present_i(),
                    "Subtitle is not present for hero with image")
        assert_that(hero_page.check_is_subtitle_label_present(),
                    "Subtitle is not present for hero without image")
