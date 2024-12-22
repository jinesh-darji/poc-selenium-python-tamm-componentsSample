from dls_auto.elements.modals.FeedbackPanel import FeedbackPanel
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class FeedbackPanelPage(BasePage):
    page_name = "Feedback Panel Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "feedback_panel_page_locator")
    feedback_panel = FeedbackPanel(locator_reader, "feedback_panel", "btn_yes", "btn_no", "txb_email", "txb_comment",
                                   "btn_next", "lbl_thanks", "chckbx_phone")

    def __init__(self):
        super(FeedbackPanelPage, self).__init__(self.page_element)

    def check_thanks_displayed_after_yes(self):
        return self.feedback_panel.is_thanks_displayed_after_yes()

    def check_thanks_not_displayed_after_no(self):
        return self.feedback_panel.is_thanks_not_displayed_after_no()

    def check_thanks_displayed_after_filling_email_comment(self):
        self.check_thanks_not_displayed_after_no()
        return self.feedback_panel.is_thanks_displayed_after_filling_email_and_comment()

