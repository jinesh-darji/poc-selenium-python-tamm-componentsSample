from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class MainPage(BasePage):
    page_name = "Main Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "main_page_locator")
    btn_menu = Button(locator_reader, "btn_menu")
    btn_buttons = Button(locator_reader, "btn_buttons")
    btn_button = Button(locator_reader, "btn_button")
    btn_view_all = Button(locator_reader, "btn_view_all")
    btn_forms = Button(locator_reader, "btn_forms")
    btn_input = Button(locator_reader, "btn_input")
    btn_phone_input = Button(locator_reader, "btn_phone_input")
    btn_select = Button(locator_reader, "btn_select")
    btn_text_area = Button(locator_reader, "btn_text_area")
    btn_upload_input = Button(locator_reader, "btn_upload_input")
    btn_load_more = Button(locator_reader, "btn_load_more")
    btn_toggle = Button(locator_reader, "btn_toggle")
    btn_smart_pass = Button(locator_reader, "btn_smart_pass")
    btn_calendar = Button(locator_reader, "btn_calendar")
    btn_download = Button(locator_reader, "btn_download")
    btn_icon = Button(locator_reader, "btn_icon")
    btn_social_share = Button(locator_reader, "btn_social_share")
    btn_upload = Button(locator_reader, "btn_upload")
    btn_accordions = Button(locator_reader, "btn_accordions")
    btn_collapse = Button(locator_reader, "btn_collapse")
    btn_event_accordion = Button(locator_reader, "btn_event_accordion")
    btn_button_dropdown = Button(locator_reader, "btn_button_dropdown")
    btn_switchers = Button(locator_reader, "btn_switchers")
    btn_content_radio = Button(locator_reader, "btn_content_radio")
    btn_checkbox = Button(locator_reader, "btn_checkbox")
    btn_radio_list = Button(locator_reader, "btn_radio_list")
    btn_search_input = Button(locator_reader, "btn_search_input")
    btn_sort_select = Button(locator_reader, "btn_sort_select")
    btn_feedback_panel = Button(locator_reader, "btn_feedback_panel")
    btn_modals = Button(locator_reader, "btn_modals")
    btn_modal = Button(locator_reader, "btn_modal")
    btn_content_checkbox = Button(locator_reader, "btn_content_checkbox")
    btn_number_selector = Button(locator_reader, "btn_number_selector")
    btn_radio_button = Button(locator_reader, "btn_radio_button")
    btn_switch_button = Button(locator_reader, "btn_switch_button")
    btn_text_size = Button(locator_reader, "btn_text_size")
    btn_theme_switcher = Button(locator_reader, "btn_theme_switcher")
    btn_content_checkbox_radio_group = Button(locator_reader, "btn_content_checkbox_radio_group")
    btn_range_slider = Button(locator_reader, "btn_range_slider")
    btn_pickers = Button(locator_reader, "btn_pickers")
    btn_date_picker = Button(locator_reader, "btn_date_picker")
    btn_pagination = Button(locator_reader, "btn_pagination")
    btn_navigations = Button(locator_reader, "btn_navigations")
    btn_prev_next_buttons = Button(locator_reader, "btn_prev_next_buttons")
    btn_breadcrumb = Button(locator_reader, "btn_breadcrumb")
    btn_emergency_footer = Button(locator_reader, "btn_emergency_footer")
    btn_footer = Button(locator_reader, "btn_footer")
    btn_header = Button(locator_reader, "btn_header")
    btn_user_menu = Button(locator_reader, "btn_user_menu")
    btn_tabs = Button(locator_reader, "btn_tabs")
    btn_notifications = Button(locator_reader, "btn_notifications")
    btn_alert = Button(locator_reader, "btn_alert")
    btn_notification = Button(locator_reader, "btn_notification")
    btn_cookie_tray = Button(locator_reader, "btn_cookie_tray")
    btn_notification_list = Button(locator_reader, "btn_notification_list")
    btn_cards = Button(locator_reader, "btn_cards")
    btn_action_card = Button(locator_reader, "btn_action_card")
    btn_appointment_card = Button(locator_reader, "btn_appointment_card")
    btn_article_card = Button(locator_reader, "btn_article_card")
    btn_card = Button(locator_reader, "btn_card")
    btn_compare_card = Button(locator_reader, "btn_compare_card")
    btn_contact_card = Button(locator_reader, "btn_contact_card")
    btn_event_card = Button(locator_reader, "btn_event_card")
    btn_location_card = Button(locator_reader, "btn_location_card")
    btn_logged_in_profile_card = Button(locator_reader, "btn_logged_in_profile_card")
    btn_profile_card = Button(locator_reader, "btn_profile_card")
    btn_plan_card = Button(locator_reader, "btn_plan_card")
    btn_small_card = Button(locator_reader, "btn_small_card")
    btn_small_description_card = Button(locator_reader, "btn_small_description_card")
    btn_summary_card = Button(locator_reader, "btn_summary_card")
    btn_fact_sheet_card = Button(locator_reader, "btn_fact_sheet_card")
    btn_label_content_card = Button(locator_reader, "btn_label_content_card")
    btn_lists = Button(locator_reader, "btn_lists")
    btn_composite_list = Button(locator_reader, "btn_composite_list")
    btn_stepper = Button(locator_reader, "btn_stepper")
    btn_vertical_stepper = Button(locator_reader, "btn_vertical_stepper")
    btn_others = Button(locator_reader, "btn_others")
    btn_social_share_panel = Button(locator_reader, "btn_social_share_panel")
    btn_table = Button(locator_reader, "btn_table")
    btn_tag = Button(locator_reader, "btn_tag")
    btn_badge = Button(locator_reader, "btn_badge")
    btn_date_time_picker = Button(locator_reader,"btn_date_time_picker")
    btn_time_picker = Button(locator_reader, "btn_time_picker")
    btn_not_found = Button(locator_reader, "btn_not_found")
    btn_hero = Button(locator_reader, "btn_hero")
    btn_progress_bar = Button(locator_reader, "btn_progress_bar")
    btn_service = Button(locator_reader, "btn_service")
    btn_nav_link = Button(locator_reader, "btn_nav_link")
    btn_carousel = Button(locator_reader, "btn_carousel")
    btn_image_gallery = Button(locator_reader, "btn_image_gallery")
    btn_spinner = Button(locator_reader, "btn_spinner")
    btn_sidebar = Button(locator_reader,"btn_sidebar")
    btn_form = Button(locator_reader,"btn_form")

    def __init__(self):
        super(MainPage, self).__init__(self.page_element)

    def collapse_menu(self):
        self.btn_menu.click()

    def open_buttons_main_menu(self):
        self.collapse_menu()
        self.btn_buttons.wait_until_location_stable()
        self.btn_buttons.click()

    def open_forms_main_menu(self):
        self.collapse_menu()
        self.btn_forms.wait_until_location_stable()
        self.btn_forms.click()

    def open_accordions_main_menu(self):
        self.collapse_menu()
        self.btn_accordions.wait_until_location_stable()
        self.btn_accordions.click()

    def open_switchers_main_menu(self):
        self.collapse_menu()
        self.btn_switchers.wait_until_location_stable()
        self.btn_switchers.click()

    def open_modals_main_menu(self):
        self.collapse_menu()
        self.btn_modals.wait_until_location_stable()
        self.btn_modals.click()

    def open_navigations_main_menu(self):
        self.collapse_menu()
        self.btn_navigations.wait_until_location_stable()
        self.btn_navigations.click()

    def open_pickers_main_menu(self):
        self.collapse_menu()
        self.btn_pickers.wait_until_location_stable()
        self.btn_pickers.click()

    def open_notifications_main_menu(self):
        self.collapse_menu()
        self.btn_notifications.wait_until_location_stable()
        self.btn_notifications.click()

    def open_cards_main_menu(self):
        self.collapse_menu()
        self.btn_cards.wait_until_location_stable()
        self.btn_cards.click()

    def open_lists_main_menu(self):
        self.collapse_menu()
        self.btn_lists.wait_until_location_stable()
        self.btn_lists.click()

    def open_others_main_menu(self):
        self.collapse_menu()
        self.btn_others.wait_until_location_stable()
        self.btn_others.click()

    def open_content_radio_button_page(self):
        self.open_switchers_main_menu()
        self.btn_content_radio.click()

    def open_checkbox_page(self):
        self.open_switchers_main_menu()
        self.btn_checkbox.click()

    def open_content_checkbox_radio_group_page(self):
        self.open_switchers_main_menu()
        self.btn_content_checkbox_radio_group.click()

    def open_range_slider_page(self):
        self.open_switchers_main_menu()
        self.btn_range_slider.click()

    def open_content_checkbox_page(self):
        self.open_switchers_main_menu()
        self.btn_content_checkbox.click()

    def open_text_size_page(self):
        self.open_switchers_main_menu()
        self.btn_text_size.click()

    def open_theme_switcher_page(self):
        self.open_switchers_main_menu()
        self.btn_theme_switcher.click()

    def open_number_selector_page(self):
        self.open_switchers_main_menu()
        self.btn_number_selector.click()

    def open_radio_button_page(self):
        self.open_switchers_main_menu()
        self.btn_radio_button.click()

    def open_switch_button_page(self):
        self.open_switchers_main_menu()
        self.btn_switch_button.click()

    def open_button_page(self):
        self.open_buttons_main_menu()
        self.btn_button.click()

    def open_view_all_button_page(self):
        self.open_buttons_main_menu()
        self.btn_view_all.click()

    def open_input_page(self):
        self.open_forms_main_menu()
        self.btn_input.click()

    def open_phone_input_page(self):
        self.open_forms_main_menu()
        self.btn_phone_input.click()

    def open_select_page(self):
        self.open_forms_main_menu()
        self.btn_select.click()

    def open_text_area_page(self):
        self.open_forms_main_menu()
        self.btn_text_area.click()

    def open_upload_input_page(self):
        self.open_forms_main_menu()
        self.btn_upload_input.click()

    def open_load_more_button_page(self):
        self.open_buttons_main_menu()
        self.btn_load_more.click()

    def open_toggle_button_page(self):
        self.open_buttons_main_menu()
        self.btn_toggle.click()

    def open_smart_pass_button_page(self):
        self.open_buttons_main_menu()
        self.btn_smart_pass.click()

    def open_calendar_button_page(self):
        self.open_buttons_main_menu()
        self.btn_calendar.click()

    def open_download_button_page(self):
        self.open_buttons_main_menu()
        self.btn_download.click()

    def open_icon_button_page(self):
        self.open_buttons_main_menu()
        self.btn_icon.click()

    def open_social_share_button_page(self):
        self.open_buttons_main_menu()
        self.btn_social_share.click()

    def open_upload_button_page(self):
        self.open_buttons_main_menu()
        self.btn_upload.click()

    def open_collapse_page(self):
        self.open_accordions_main_menu()
        self.btn_collapse.click()

    def open_button_dropdown_page(self):
        self.open_forms_main_menu()
        self.btn_button_dropdown.click()

    def open_event_accordion_page(self):
        self.open_accordions_main_menu()
        self.btn_event_accordion.click()

    def open_radio_list_page(self):
        self.open_forms_main_menu()
        self.btn_radio_list.click()

    def open_search_input_page(self):
        self.open_forms_main_menu()
        self.btn_search_input.click()

    def open_sort_select_page(self):
        self.open_forms_main_menu()
        self.btn_sort_select.click()

    def open_feedback_panel_page(self):
        self.open_modals_main_menu()
        self.btn_feedback_panel.click()

    def open_modal_page(self):
        self.open_modals_main_menu()
        self.btn_modal.click()

    def open_date_picker_page(self):
        self.open_pickers_main_menu()
        self.btn_date_picker.click()

    def open_pagination_page(self):
        self.open_navigations_main_menu()
        self.btn_pagination.click()

    def open_prev_next_buttons_page(self):
        self.open_navigations_main_menu()
        self.btn_prev_next_buttons.click()

    def open_breadcrumb_page(self):
        self.open_navigations_main_menu()
        self.btn_breadcrumb.click()

    def open_emergency_footer_page(self):
        self.open_navigations_main_menu()
        self.btn_emergency_footer.click()

    def open_footer_page(self):
        self.open_navigations_main_menu()
        self.btn_footer.click()

    def open_header_page(self):
        self.open_navigations_main_menu()
        self.btn_header.click()

    def open_user_menu_page(self):
        self.open_navigations_main_menu()
        self.btn_user_menu.click()

    def open_tabs_page(self):
        self.open_navigations_main_menu()
        self.btn_tabs.click()

    def open_alert_page(self):
        self.open_notifications_main_menu()
        self.btn_alert.click()

    def open_notification_page(self):
        self.open_notifications_main_menu()
        self.btn_notification.click()

    def open_cookie_tray_page(self):
        self.open_notifications_main_menu()
        self.btn_cookie_tray.click()

    def open_notification_list_page(self):
        self.open_notifications_main_menu()
        self.btn_notification_list.click()

    def open_action_card_page(self):
        self.open_cards_main_menu()
        self.btn_action_card.click()

    def open_appointment_card_page(self):
        self.open_cards_main_menu()
        self.btn_appointment_card.click()

    def open_article_card_page(self):
        self.open_cards_main_menu()
        self.btn_article_card.click()

    def open_card_page(self):
        self.open_cards_main_menu()
        self.btn_card.click()

    def open_compare_card_page(self):
        self.open_cards_main_menu()
        self.btn_compare_card.click()

    def open_contact_card_page(self):
        self.open_cards_main_menu()
        self.btn_contact_card.click()

    def open_event_card_page(self):
        self.open_cards_main_menu()
        self.btn_event_card.click()

    def open_location_card_page(self):
        self.open_cards_main_menu()
        self.btn_location_card.click()

    def open_logged_in_profile_card_page(self):
        self.open_cards_main_menu()
        self.btn_logged_in_profile_card.click()

    def open_profile_card_page(self):
        self.open_cards_main_menu()
        self.btn_profile_card.click()

    def open_plan_card_page(self):
        self.open_cards_main_menu()
        self.btn_plan_card.click()

    def open_small_card_page(self):
        self.open_cards_main_menu()
        self.btn_small_card.click()

    def open_small_description_card_page(self):
        self.open_cards_main_menu()
        self.btn_small_description_card.click()

    def open_summary_card_page(self):
        self.open_cards_main_menu()
        self.btn_summary_card.click()

    def open_fact_sheet_card_page(self):
        self.open_cards_main_menu()
        self.btn_fact_sheet_card.click()

    def open_label_content_card_page(self):
        self.open_cards_main_menu()
        self.btn_label_content_card.click()

    def open_composite_list_page(self):
        self.open_lists_main_menu()
        self.btn_composite_list.click()

    def open_stepper_page(self):
        self.open_lists_main_menu()
        self.btn_stepper.click()

    def open_vertical_stepper_page(self):
        self.open_lists_main_menu()
        self.btn_vertical_stepper.click()

    def open_social_share_panel_page(self):
        self.open_others_main_menu()
        self.btn_social_share_panel.click()

    def open_table_page(self):
        self.open_others_main_menu()
        self.btn_table.click()

    def open_tag_page(self):
        self.open_others_main_menu()
        self.btn_tag.click()

    def open_badge_page(self):
        self.open_others_main_menu()
        self.btn_badge.click()

    def open_date_time_picker_page(self):
        self.open_pickers_main_menu()
        self.btn_date_time_picker.wait_until_location_stable()
        self.btn_date_time_picker.click()

    def open_not_found_page(self):
        self.open_others_main_menu()
        self.btn_not_found.click()

    def open_hero_page(self):
        self.open_others_main_menu()
        self.btn_hero.click()

    def open_progress_bar_page(self):
        self.open_others_main_menu()
        self.btn_progress_bar.click()

    def open_service_page(self):
        self.open_others_main_menu()
        self.btn_service.click()

    def open_nav_link_page(self):
        self.open_others_main_menu()
        self.btn_nav_link.click()

    def open_carousel_page(self):
        self.open_others_main_menu()
        self.btn_carousel.click()

    def open_image_gallery_page(self):
        self.open_others_main_menu()
        self.btn_image_gallery.click()

    def open_spinner_page(self):
        self.open_others_main_menu()
        self.btn_spinner.click()

    def open_time_picker_page(self):
        self.open_pickers_main_menu()
        self.btn_time_picker.wait_until_location_stable()
        self.btn_time_picker.click()

    def open_sidebar_page(self):
        self.open_navigations_main_menu()
        self.btn_sidebar.click()

    def open_form_page(self):
        self.open_forms_main_menu()
        self.btn_form.click()