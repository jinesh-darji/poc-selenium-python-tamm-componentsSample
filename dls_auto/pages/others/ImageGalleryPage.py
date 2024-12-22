from dls_auto.elements.others.ImageGallery import ImageGallery
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ImageGalleryPage(BasePage):
    page_name = "Image Gallery Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "image_gallery_page_locator")
    image_gallery = ImageGallery(locator_reader, "image_gallery", "btn_left", "btn_right", "btn_image", "lbl_selected_image")

    ELEMENTS_COUNT = 6

    def __init__(self):
        super(ImageGalleryPage, self).__init__(self.page_element)

    def check_is_left_disabled(self):
        return self.image_gallery.is_left_disabled()

    def check_is_right_disabled(self):
        for i in range(self.ELEMENTS_COUNT):
            self.image_gallery.btn_right.wait_until_location_stable()
            self.image_gallery.btn_right.click()
        return self.image_gallery.is_right_disabled()

    def check_is_button_active_when_clicked(self):
        self.image_gallery.btn_image.wait_until_location_stable()
        self.image_gallery.btn_image.click()
        self.image_gallery.btn_image.wait_until_location_stable()
        return self.image_gallery.is_button_active()
