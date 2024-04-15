from pages.form_page import FormPage


# Fixtures: driver, fake, form_conditions:
def test_register_btn_unblocked(driver, fake, form_conditions):
    # Pre-conditions...
    # Test:
    page = FormPage(driver, form_conditions)

    page.form_email().send_keys(fake.email())
    page.form_pass().send_keys(fake.password())

    checkbox = page.form_checkbox()
    checkbox.click()

    assert checkbox.is_selected(), 'Checkbox is not checked'

    register_btn = page.form_btn()
    assert register_btn.is_enabled(), 'Continue button is blocked'

    # Post-conditions...
