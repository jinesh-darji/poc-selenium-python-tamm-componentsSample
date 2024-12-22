from dls_auto.elements.others.Tag import Tag
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TagPage(BasePage):
    page_name = "Tag Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "tag_page_locator")
    tag = Tag(locator_reader, "tag", "btn_close")

    def __init__(self):
        super(TagPage, self).__init__(self.page_element)

    def check_is_tag_closed(self):
        return self.tag.is_tag_closed()
