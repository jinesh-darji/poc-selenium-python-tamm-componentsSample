# coding=utf-8
from framework.browser.Browser import Browser
from framework.elements.Button import Button
from framework.elements.base.BaseElement import BaseElement


class NavLink(BaseElement):
    def __init__(self, locator_reader, element_key, btn_back, btn_forward, btn_page):
        super(NavLink, self).__init__(locator_reader, element_key)
        self.btn_back = Button(locator_reader, btn_back)
        self.btn_forward = Button(locator_reader, btn_forward)
        self.btn_page = Button(locator_reader, btn_page)

    def get_element_type(self):
        return "NavLink"

    def is_btn_back_redirects(self):
        self.btn_back.click()
        result = not self.btn_back.is_present()
        if result:
            Browser.back_page()
        return result

    def is_btn_page_redirects(self):
        self.btn_page.click()
        result = not self.btn_page.is_present()
        if result:
            Browser.back_page()
        return result

    def is_btn_forward_redirects(self):
        self.btn_forward.click()
        result = not self.btn_forward.is_present()
        if result:
            Browser.back_page()
        return result
