import allure
from selene import have

from tests.UI.pages.main_page import MainPage
from tests.UI.pages.serp_page import Serp

mainpage = MainPage()
serp = Serp()


@allure.feature('Серповый поиск')
@allure.title('Поиск на двух взрослых')
def test_search_for_two_adults(open_browser):
    serp.open('ozersk', '31.10.2023', '01.11.2023', "2")

    serp.price_notice.should(have.texts(
        ['for a night for 2 guests' for x in range(len(serp.price_notice))]
    ))


@allure.feature('Серповый поиск')
@allure.title('Поиск на двух взрослых и ребенка')
def test_search_for_two_adults_and_one_child(open_browser):
    serp.open('moscow', '31.10.2023', '01.11.2023', "2and1")

    serp.price_notice.should(have.texts(
        ['for a night for 2 guests and 1 child' for x in range(len(serp.price_notice))]
    ))




