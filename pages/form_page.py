from pages.base_page import BasePage

from locators.form_data import FormData
from locators.form_locs import FormLocs


class FormPage(BasePage):
    def open(self):
        self.driver.get(FormData.form_url)

    def form_header(self):
        return self.is_visible(FormLocs.form_header)

    def form_container(self):
        return self.is_visible(FormLocs.form_container)

    def form_email(self):
        return self.is_visible(FormLocs.form_email)

    def form_pass(self):
        return self.is_visible(FormLocs.form_pass)

    def form_checkbox(self):
        return self.find_el(FormLocs.form_checkbox)

    def form_btn(self):
        return self.is_visible(FormLocs.form_btn)
