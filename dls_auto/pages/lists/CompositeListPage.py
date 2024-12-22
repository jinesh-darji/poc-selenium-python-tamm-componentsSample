from dls_auto.elements.lists.ListHeading import ListHeading
from dls_auto.elements.lists.SelectList import SelectList
from dls_auto.elements.lists.ToDoList import ToDoList
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CompositeListPage(BasePage):
    page_name = "Composite List Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "composite_list_page_locator")
    list_heading = ListHeading(locator_reader, "list_heading", "lbl_title_heading", "lbl_description_heading", "btn_complete_heading",
                               "chckbx_complete_heading",
                               "btn_arrow_heading")
    to_do_list = ToDoList(locator_reader, "to_do_list", "lbl_title_todo", "btn_complete_todo", "chckbx_complete_todo", "btn_arrow")
    multi_select_list = SelectList(locator_reader, "multi_select_list", "lbl_title_multi", "lbl_item_title_multi",
                                   "lbl_item_description_multi",
                                   "btn_complete_multi", "chckbx_complete_multi")
    single_select_list = SelectList(locator_reader, "single_select_list", "lbl_title_single", "lbl_item_title_single",
                                    "lbl_item_description_single",
                                    "btn_complete_single", "chckbx_complete_single")

    def __init__(self):
        super(CompositeListPage, self).__init__(self.page_element)
