from hamcrest import assert_that
from dls_auto.pages.MainPage import MainPage
from dls_auto.pages.cards.ArticleCardPage import ArticleCardPage
from framework.browser.Browser import Browser


class TestArticleCardElement:
    def test_article_card_element(self):
        main_page = MainPage()
        main_page.open_article_card_page()
        main_page.btn_menu.click()
        article_card_page = ArticleCardPage()
        Browser.scroll_to_top()
        assert_that(article_card_page.check_is_card_has_image(), "Card does not have background image")
        assert_that(article_card_page.check_is_card_has_title(), "Card does not have title")
        assert_that(article_card_page.check_is_card_has_body(), "Card does not have body")
        assert_that(article_card_page.check_is_card_has_btn_read(), "Card does not have Read More button")