from dls_auto.elements.cards.ArticleCard import ArticleCard
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ArticleCardPage(BasePage):
    page_name = "Article Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "article_card_page_locator")
    article_card = ArticleCard(locator_reader, "article_card", "lbl_image", "lbl_title",
                               "lbl_body", "btn_read")

    def __init__(self):
        super(ArticleCardPage, self).__init__(self.page_element)

    def check_is_card_has_image(self):
        return self.article_card.is_card_has_image()

    def check_is_card_has_title(self):
        return self.article_card.is_card_has_title()

    def check_is_card_has_body(self):
        return self.article_card.is_card_has_body()

    def check_is_card_has_btn_read(self):
        return self.article_card.is_card_has_btn_read()