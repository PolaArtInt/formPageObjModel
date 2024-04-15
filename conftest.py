import pytest
from selenium import webdriver

from pages.form_page import FormPage
from locators.form_data import FormData


# driver init:
@pytest.fixture(scope="function", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    # chrome_options.add_argument("--headless")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=1280,1000")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture()
def fake():
    from faker import Faker
    fake = Faker()
    return fake


@pytest.fixture()
def form_conditions(driver):
    # Pre-conditions:
    # 1. Navigate to url
    page = FormPage(driver, FormData.form_url)
    page.open()

    assert driver.current_url == FormData.form_url and \
           page.form_header().text == 'Sign in to your account'

    # 2. Check if form fields are empty
    # 3. Clear form fields
    email_field = page.form_email()
    pass_field = page.form_pass()
    check_field = page.form_checkbox()

    if check_field.is_selected() or email_field.text != '' or pass_field.text != '':
        check_field.click()
        email_field.clear()
        pass_field.clear()

    assert email_field.text == '', 'Input Email is filled'
    assert pass_field.text == '', 'Input Password is filled'
    assert not check_field.is_selected(), 'Checkbox is selected'

    # Test:
    yield form_conditions

    # Post-conditions:
    page.refresh()
