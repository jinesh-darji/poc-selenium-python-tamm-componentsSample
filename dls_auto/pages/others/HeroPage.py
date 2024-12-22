from dls_auto.elements.others.Hero import Hero
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class HeroPage(BasePage):
    page_name = "Hero Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "hero_page_locator")
    hero_with_image = Hero(locator_reader, "hero_with_image", "lbl_image_i", "lbl_title_i", "lbl_subtitle_i")
    hero_no_image = Hero(locator_reader, "hero_no_image", "lbl_image", "lbl_title", "lbl_subtitle")

    def __init__(self):
        super(HeroPage, self).__init__(self.page_element)

    def check_is_title_label_present_i(self):
        return self.hero_with_image.is_title_label_present()

    def check_is_title_label_present(self):
        return self.hero_no_image.is_title_label_present()

    def check_is_subtitle_label_present_i(self):
        return self.hero_with_image.is_subtitle_label_present()

    def check_is_subtitle_label_present(self):
        return self.hero_no_image.is_subtitle_label_present()

    def check_is_image_label_present_i(self):
        return self.hero_with_image.is_image_label_present()

    def check_is_image_label_not_present(self):
        return not self.hero_no_image.is_image_label_present()
