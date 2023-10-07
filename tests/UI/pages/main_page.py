from selene import browser, by, be, have
import allure
import os


class MainPage:
    def __init__(self):
        # Login button and form
        self.login_entry = browser.element(by.text('Log in'))
        self.login_input = browser.element('[data-testid="user-widget-sign-in-email-input"]')
        self.password_input = browser.element('[data-testid="user-widget-sign-in-password-input"]')
        self.login_button = browser.element('[data-testid="user-widget-sign-in-button"]')
        self.logged_in_user_email = browser.element('[data-testid="user-widget-control"]')

        # Search form
        self.destination_input = browser.element('[data-testid="destination-input"]')
        self.search_button = browser.element('[data-testid="search-button"]')
        self.checkin_date = browser.element('[data-testid="date-start-input"]')
        self.checkout_date = browser.element('[data-testid="date-end-input"]')

        # Suggest items
        self.first_region = browser.all('[class*="Suggest-module"][role="button"]').first
        self.first_hotel = browser.all('[class*="Suggest-module"][role="button"]')[5]

    def login(self):
        with allure.step(f"Вызов формы логина в хэдере"):
            self.login_entry.click()

        with allure.step(f"Ввод логина и пароля"):
            self.login_input.clear().type(os.getenv('SITE_USERNAME'))
            self.password_input.clear().type(os.getenv('SITE_PASSWORD'))

        with allure.step(f"Сабмит данных"):
            self.login_button.click()

        with allure.step(f"Проверка успешности логина"):
            self.logged_in_user_email.should(be.visible)

    def fill_destination(self, region_or_hotel: str):
        with allure.step(f"Ввод текста {region_or_hotel} в инпут направления"):
            self.destination_input.clear().type(region_or_hotel)

        with allure.step(f"Выбор значения {region_or_hotel} из автокомплита"):
            self.first_region.should(have.text(region_or_hotel))
            self.first_region.click()

    def do_search(self):
        with allure.step(f"Нажатие кнопки 'Поиск'"):
            self.search_button.click()

