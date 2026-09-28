import uuid
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, RegistrationDialogLocators, LoginDialogLocators
from helpers import Helpers as h


BASE_URL = "https://qa-desk.education-services.ru/"


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия браузера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def open_register_form(driver):
    """
    Фикстура открытия диалога регистрации.
    """
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(StartPageLocators.ENTER_AND_REGISTER_BUTTON))
    driver.find_element(*StartPageLocators.ENTER_AND_REGISTER_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginDialogLocators.HAVENT_ACCOUNT_BUTTON))
    driver.find_element(*LoginDialogLocators.HAVENT_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON))
    return driver


@pytest.fixture
def open_register_form_for_existing_user(driver):
    """
    Фикстура открытия диалога регистрации.
    """
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(StartPageLocators.ENTER_AND_REGISTER_BUTTON))
    driver.find_element(*StartPageLocators.ENTER_AND_REGISTER_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginDialogLocators.HAVENT_ACCOUNT_BUTTON))
    driver.find_element(*LoginDialogLocators.HAVENT_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON))
    return driver


@pytest.fixture
def registered_user_email(open_register_form):
    """
    Фикстура регистрирует случайного пользователя в системе, 
    чтобы он гарантированно стал 'существующим'.
    """
    driver = open_register_form
    random_email = h.random_email
    driver.find_element(
        *RegistrationDialogLocators.EMAIL_FIELD).send_keys(random_email)
    driver.find_element(
        *RegistrationDialogLocators.PASSWORD_FIELD).send_keys(h.password)
    driver.find_element(
        *RegistrationDialogLocators.PASSWORD_CONFIRMATION_FIELD).send_keys(h.password)
    driver.find_element(
        *RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.invisibility_of_element_located(RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON))

    driver.delete_all_cookies()

    driver.find_element(
        *StartPageLocators.LOGOUT_BUTTON).click()

    return random_email


@pytest.fixture
def process_email(request):
    return request.getfixturevalue(request.param)


@pytest.fixture
def open_login_form(driver):
    """
    Фикстура открытия диалога логина.
    """
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(StartPageLocators.ENTER_AND_REGISTER_BUTTON))
    driver.find_element(*StartPageLocators.ENTER_AND_REGISTER_BUTTON).click()
    return driver


@pytest.fixture
def login_user(registered_user_email, open_login_form):
    """
    Фикстура логина пользователя.
    """
    driver = open_login_form
    driver.find_element(
        *LoginDialogLocators.EMAIL_FIELD).send_keys(registered_user_email)
    driver.find_element(
        *LoginDialogLocators.PASSWORD_FIELD).send_keys(h.password)

    driver.find_element(*LoginDialogLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3, 1).until(
        expected_conditions.invisibility_of_element_located(LoginDialogLocators.ENTER_BUTTON))

    return driver
