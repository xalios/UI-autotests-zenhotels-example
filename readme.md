## Пример организации кода UI-автотестов для тестирования сайта бронирований Zenhotels.com

## Реализованные сценарии:

* Проверка авторизации пользователя
* Проверка регионального поиска
* Проверка отельного поиска
* Проверка поиска для взрослых/детей

## Применяемые технологии

<table>
    <tr>
        <td><img src="img/pysharm.png" width="48" height="48"  alt="PyCharm"/></td>
        <td>Pycharm</td>
    </tr>
    <tr>
        <td><img src="img/python.png" width="48" height="48"  alt="Python"/></td>
        <td>Python</td>
    </tr>
    <tr>
        <td><img src="img/pytest.png" width="48" height="48"  alt="Pytest"/></td>
        <td>Pytest</td>
    </tr>
    <tr>
        <td><img src="img/selene.png" width="48" height="48"  alt="Selene"/></td>
        <td>Selene</td>
    </tr>
    <tr>
        <td><img src="img/selenoid.png" width="48" height="48"  alt="Selenoid"/></td>
        <td>Selenoid</td>
    </tr>
    <tr>
        <td><img src="img/jenkins.svg" width="40" height="48"  alt="Jenkins"/></td>
        <td>Jenkins</td>
    </tr>
    <tr>
        <td><img src="img/allure.png" width="48" height="48"  alt="Allure"/></td>
        <td>Allure</td>
    </tr>
</table>

## Запуск

1. Зарегистрировать пользователя на сайте Zenhotels.com
2. Заполнить значения переменных SITE_USERNAME, SITE_PASSWORD, SELENOID_USERNAME, SELENOID_PASSWORD в файле .env.example.
3. Файл .env.example переименовать в .env
4. Создать локальное окружение и активировать его:
```bash
python -m venv .venv
source .venv/bin/activate
```
5. Установить зависимости:
```bash
pip install -r requirements.txt
```
6. Запустить тесты:
```bash
pytest .
```

## Скриншоты Allure-отчета

<img src="img/allure-report.png" width=75% height=75%  alt="Allure-report"/>
<img src="img/allure-report2.png" width=50% height=50%  alt="Allure-report"/>