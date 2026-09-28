import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, RegistrationDialogLocators


class TestRegistration:

    def test_registration_successful_avatar_and_name_visible(self, open_register_form, random_email, password):
        driver = open_register_form
        driver.find_element(
            *RegistrationDialogLocators.EMAIL_FIELD).send_keys(random_email)
        driver.find_element(
            *RegistrationDialogLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(
            *RegistrationDialogLocators.PASSWORD_CONFIRMATION_FIELD).send_keys(password)
        driver.find_element(
            *RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.invisibility_of_element_located(RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON))
        assert driver.find_element(
            *StartPageLocators.AVATAR).is_displayed
        assert driver.find_element(
            *StartPageLocators.NAME).text == 'User.'

    @pytest.mark.parametrize(
        "email_type, process_email",
        [
            ("invalid email", "invalid_email"),
            ("existing email", "registered_user_email"),
        ],
        indirect=["process_email"]
    )
    def test_registration_unsuccessful_error_message_visible(self, email_type, process_email, password, open_register_form_for_existing_user):
        driver = open_register_form_for_existing_user
        driver.find_element(
            *RegistrationDialogLocators.EMAIL_FIELD).send_keys(process_email)
        driver.find_element(
            *RegistrationDialogLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(
            *RegistrationDialogLocators.PASSWORD_CONFIRMATION_FIELD).send_keys(password)
        driver.find_element(
            *RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationDialogLocators.ERROR_TEXT))

        assert driver.find_element(
            *RegistrationDialogLocators.ERROR_TEXT).text == "Ошибка"
