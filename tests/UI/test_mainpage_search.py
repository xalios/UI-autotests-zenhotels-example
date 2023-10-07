import os
import allure
import pytest
from selene import have

from tests.UI.pages.hotel_page import HotelPage
from tests.UI.pages.main_page import MainPage
from tests.UI.pages.serp_page import Serp

mainpage = MainPage()
serp = Serp()
hotelpage = HotelPage()


@allure.feature('Логин')
@allure.title('Логин b2c пользователем')
def test_login(open_browser):
    mainpage.login()

    mainpage.logged_in_user_email.should(have.text(os.environ.get('SITE_USERNAME')))


@allure.feature('Поиск с главной страницы')
@allure.title('Региональный поиск')
@pytest.mark.parametrize('region_name', ['Berlin', 'Moscow'])
def test_regional_search(open_browser, region_name):
    mainpage.fill_destination(region_name)
    mainpage.do_search()

    serp.result_title.should(have.text(region_name))


@allure.feature('Поиск с главной страницы')
@allure.title('Отельный поиск')
@pytest.mark.parametrize('hotel_name', ['Aqua Blue', 'Juli reception'])
def test_hotel_search(open_browser, hotel_name):
    mainpage.fill_destination(hotel_name)
    mainpage.do_search()

    hotelpage.hotel_title.should(have.text(hotel_name))


