from framework.elements.base.BaseElement import BaseElement


class CalendarButton(BaseElement):

    def __init__(self, locator_reader, element_key):
        super(CalendarButton, self).__init__(locator_reader, element_key)

    def get_element_type(self):
        return "CalendarButton"

    def is_button_calendar(self):
        return "uil-calendar-button__button ant-dropdown-trigger" in self.get_attribute("class")

    def is_button_collapsed(self):
        return "hidden" not in self.get_attribute("class")
