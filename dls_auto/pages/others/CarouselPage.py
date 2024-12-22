from dls_auto.elements.others.Carousel import Carousel
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CarouselPage(BasePage):
    page_name = "Carousel Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "carousel_page_locator")
    carousel_vertical = Carousel(locator_reader, "carousel_vertical", "lbl_vertical_title", "btn_vertical_carousel")
    carousel_horizontal = Carousel(locator_reader, "carousel_horizontal", "lbl_horizontal_title", "btn_horizontal_carousel")

    def __init__(self):
        super(CarouselPage, self).__init__(self.page_element)

    def check_is_image_change_when_click_vert(self):
        return self.carousel_vertical.is_image_change_when_click()

    def check_is_image_change_when_click_hor(self):
        return self.carousel_horizontal.is_image_change_when_click()