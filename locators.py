from dataclasses import dataclass
from enum import Enum
from selenium.webdriver.common.by import By


@dataclass
class StartPageLocators:
    ENTER_AND_REGISTER_BUTTON = {
        'by': By.XPATH,
        'locator': "//button[contains(text(),'Вход и регистрация')]"
    }
    PUSH_AD_BUTTON = {
        'by': By.XPATH,
        'locator': '//button[text()="Разместить объявление"]'
    }
    LOGOUT_BUTTON = {
        'by': By.XPATH,
        'locator': '//button[text()="Выйти"]'
    }
    AVATAR = {
        'by': By.CLASS_NAME,
        'locator': 'circleSmall'
    }
    NAME = {
        'by': By.XPATH,
        'locator': '//h3[@class="profileText name"]'
    }
    MODAL_VIEW = {
        'by': By.XPATH,
        'locator': '//form//h1[text()="Чтобы разместить объявление, авторизуйтесь"]'
    }
# Если следовать буквально заданию "рядом с кнопкой разместить объявление", то такой локатор
# для имени '//button[text()="Разместить объявление"]/preceding-sibling::div//h3[@class="profileText name"]'
# для аватара '//button[text()="Разместить объявление"]/preceding-sibling::div//*[@class="circleSmall"]'


@dataclass
class LoginDialogLocators:
    EMAIL_FIELD = {
        'by': By.XPATH,
        'locator': '//form//h1[text()="Войти"]/ancestor::form//input[@name="email"]'
    }
    PASSWORD_FIELD = {
        'by': By.XPATH,
        'locator': '//form//h1[text()="Войти"]/ancestor::form//input[@name="password"]'
    }
    ENTER_BUTTON = {
        'by': By.XPATH,
        'locator': '//form//h1[text()="Войти"]/ancestor::form//button[text()="Войти"]'
    }
    HAVENT_ACCOUNT_BUTTON = {
        'by': By.XPATH,
        'locator': '//form//h1[text()="Войти"]/ancestor::form//button[text()="Нет аккаунта"]'
    }


@dataclass
class RegistrationDialogLocators:
    EMAIL_FIELD = {
        'by': By.XPATH,
        'locator': "//form//h1[text()='Зарегистрироваться']/ancestor::form//input[@name='email']"
    }
    PASSWORD_FIELD = {
        'by': By.XPATH,
        'locator': '//form//h1[text()="Зарегистрироваться"]/ancestor::form//input[@name="password"]'
    }
    PASSWORD_CONFIRMATION_FIELD = {
        'by': By.XPATH,
        'locator': '//form//h1[text()="Зарегистрироваться"]/ancestor::form//input[@name="submitPassword"]'
    }
    CREATE_ACCOUNT_BUTTON = {
        'by': By.XPATH,
        'locator': '//form//h1[text()="Зарегистрироваться"]/ancestor::form//button[text()="Создать аккаунт"]'
    }
    ERROR_TEXT = {
        "by": By.XPATH,
        "locator": EMAIL_FIELD["locator"]+"/parent::div/parent::div/following-sibling::span"
    }


class AdvertisementFormLocators:
    NAME_INPUT = {
        'by': By.XPATH,
        'locator': '//div[starts-with(@class,"createListing_inputRow")]//input[@name="name"]'
    }
    CATEGORY_DROPDOWN_BUTTON = {
        'by': By.XPATH,
        'locator': '//div[starts-with(@class,"dropDownMenu_input")]//input[@name="category"]/following-sibling::button[contains(@class,"arrowDown")]'
    }
    CATEGORY_DROPDOWN_MENU = {
        'by': By.XPATH,
        'locator': '//div[starts-with(@class,"dropDownMenu_input")]//input[@name="category"]/parent::div/following-sibling::div[starts-with(@class,"dropDownMenu_options")]/button[contains(@class,"dropDownMenu_btn")]'
    }
    CONDITION_RADIO = {
        'by': By.XPATH,
        'locator': '//fieldset[starts-with(@class,"createListing_inputRadio")]//input[@type="radio" and @name="condition"]'
    }
    CONDITION_RADIO_UNSLECTED = {
        'by': By.XPATH,
        'locator': '//fieldset[starts-with(@class,"createListing_inputRadio")]//input[@type="radio" and @name="condition"]/following-sibling::div[starts-with(@class,"radioUnput_inputRegular")]'
    }
    CITY_DROPDOWN_BUTTON = {
        'by': By.XPATH,
        'locator': '//div[starts-with(@class,"dropDownMenu_input")]//input[@name="city"]/following-sibling::button[starts-with(@class,"dropDownMenu_arrowDown")]'
    }
    CITY_DROPDOWN_MENU = {
        'by': By.XPATH,
        'locator': '//div[starts-with(@class,"dropDownMenu_input")]//input[@name="city"]/parent::div/following-sibling::div[starts-with(@class,"dropDownMenu_options")]/button[contains(@class,"dropDownMenu_btn")]'
    }
    DESCRIPTION_TEXTAREA = {
        'by': By.XPATH,
        'locator': '//textarea[@name="description"]'
    }
    PRICE_INPUT = {
        'by': By.XPATH,
        'locator': '//div[starts-with(@class,"input_inputDefault")]//input[@name="price"]'
    }
    PUBLISH_BUTTON = {
        'by': By.XPATH,
        'locator': '//button[text()="Опубликовать"]'
    }


class ProfilePageLocators:
    MY_ADS_HEADING = {
        'by': By.XPATH,
        'locator': '//h1[text()="Мои объявления"]'
    }
    TARGET_ADVERTISEMENT = {
        'by': By.XPATH,
        'locator': '//h1[text()="Мои объявления"]/following-sibling::div//div[@class="card"]//h2'
    }
