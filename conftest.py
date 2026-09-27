import uuid
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, RegistrationDialogLocators, LoginDialogLocators


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
        expected_conditions.visibility_of_element_located((StartPageLocators.ENTER_AND_REGISTER_BUTTON['by'],
                                                           StartPageLocators.ENTER_AND_REGISTER_BUTTON['locator'])))
    driver.find_element(StartPageLocators.ENTER_AND_REGISTER_BUTTON['by'],
                        StartPageLocators.ENTER_AND_REGISTER_BUTTON['locator']).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((LoginDialogLocators.HAVENT_ACCOUNT_BUTTON['by'],
                                                           LoginDialogLocators.HAVENT_ACCOUNT_BUTTON['locator'])))
    driver.find_element(LoginDialogLocators.HAVENT_ACCOUNT_BUTTON['by'],
                        LoginDialogLocators.HAVENT_ACCOUNT_BUTTON['locator']).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['by'],
                                                           RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['locator'])))
    return driver


@pytest.fixture
def random_email():
    """
    Генерирует уникальный email формата *******@*******.com
    """
    _uid = uuid.uuid4().hex
    email = _uid[:7]+'@'+_uid[-7:]+'.'+'com'

    return email


@pytest.fixture
def password():
    return "Password$123"


@pytest.fixture
def invalid_email():
    return "invalid_email.com"


@pytest.fixture
def open_register_form_for_existing_user(driver):
    """
    Фикстура открытия диалога регистрации.
    """
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((StartPageLocators.ENTER_AND_REGISTER_BUTTON['by'],
                                                           StartPageLocators.ENTER_AND_REGISTER_BUTTON['locator'])))
    driver.find_element(StartPageLocators.ENTER_AND_REGISTER_BUTTON['by'],
                        StartPageLocators.ENTER_AND_REGISTER_BUTTON['locator']).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((LoginDialogLocators.HAVENT_ACCOUNT_BUTTON['by'],
                                                           LoginDialogLocators.HAVENT_ACCOUNT_BUTTON['locator'])))
    driver.find_element(LoginDialogLocators.HAVENT_ACCOUNT_BUTTON['by'],
                        LoginDialogLocators.HAVENT_ACCOUNT_BUTTON['locator']).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['by'],
                                                           RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['locator'])))
    return driver


@pytest.fixture
def registered_user_email(open_register_form, random_email, password):
    """
    Фикстура регистрирует случайного пользователя в системе, 
    чтобы он гарантированно стал 'существующим'.
    """
    driver = open_register_form

    driver.find_element(RegistrationDialogLocators.EMAIL_FIELD['by'],
                        RegistrationDialogLocators.EMAIL_FIELD['locator']).send_keys(random_email)
    driver.find_element(RegistrationDialogLocators.PASSWORD_FIELD['by'],
                        RegistrationDialogLocators.PASSWORD_FIELD['locator']).send_keys(password)
    driver.find_element(RegistrationDialogLocators.PASSWORD_CONFIRMATION_FIELD['by'],
                        RegistrationDialogLocators.PASSWORD_CONFIRMATION_FIELD['locator']).send_keys(password)
    driver.find_element(RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['by'],
                        RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['locator']).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.invisibility_of_element_located((RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['by'],
                                                             RegistrationDialogLocators.CREATE_ACCOUNT_BUTTON['locator'])))

    driver.delete_all_cookies()

    driver.find_element(
        StartPageLocators.LOGOUT_BUTTON['by'], StartPageLocators.LOGOUT_BUTTON['locator']).click()

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
        expected_conditions.visibility_of_element_located((StartPageLocators.ENTER_AND_REGISTER_BUTTON['by'],
                                                           StartPageLocators.ENTER_AND_REGISTER_BUTTON['locator'])))
    driver.find_element(StartPageLocators.ENTER_AND_REGISTER_BUTTON['by'],
                        StartPageLocators.ENTER_AND_REGISTER_BUTTON['locator']).click()
    return driver


@pytest.fixture
def login_user(registered_user_email, open_login_form, password):
    """
    Фикстура логина пользователя.
    """
    driver = open_login_form
    driver.find_element(LoginDialogLocators.EMAIL_FIELD['by'],
                        LoginDialogLocators.EMAIL_FIELD['locator']).send_keys(registered_user_email)
    driver.find_element(LoginDialogLocators.PASSWORD_FIELD['by'],
                        LoginDialogLocators.PASSWORD_FIELD['locator']).send_keys(password)

    driver.find_element(LoginDialogLocators.ENTER_BUTTON['by'],
                        LoginDialogLocators.ENTER_BUTTON['locator']).click()
    WebDriverWait(driver, 3, 1).until(
        expected_conditions.invisibility_of_element_located((LoginDialogLocators.ENTER_BUTTON['by'],
                                                             LoginDialogLocators.ENTER_BUTTON['locator'])))

    return driver


@pytest.fixture
def new_advert_name():
    return "Прекрасное объявление"


@pytest.fixture
def new_advert_description():
    return "Описание Прекрасного объявления"


@pytest.fixture
def new_advert_price():
    return 123
