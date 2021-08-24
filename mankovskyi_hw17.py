"""
Реализовать функционал получения информации о городе посредством Python.

User Story: При запуске файла пользователь вводит название города, система возвращает название города, страну, валюту и количество населения

Tech Requirements:

Ввод реализовать с помощью CLI интерфейса. Выбор WEB-API для получения информации - на усмотрение разработчика.
Код должен быть читаемым, с комментариями и соответствовать принципам DRY, KISS, YAGNI.
Кд должен быть загружен на GitHub или GitLab как отдельный проект с публичным доступом.
Формат вывода только такой как в примере

"""

from geopy.geocoders import Nominatim
from countryinfo import CountryInfo


def diploma():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(
        input('Введите городишко(поиск регистронезависимый, не отказывайте себе в фантазии): \n'),
        addressdetails=True, extratags=True, language='en')
    loc_dict = location.raw

    city = loc_dict['display_name']
    city = city.split(',')[0]

    try:
        print('City:', city)
    except KeyError:
        print('Ошибка провайдера данных. Невозможно получить город для данной страны')

    try:
        print('Country:', loc_dict['address']['country'])
    except KeyError:
        print('Ошибка провайдера данных. Невозможно получить название страны')
    try:
        print('Population', loc_dict['extratags']['population'])
    except KeyError:
        print('Ошибка провайдера данных. Невозможно получить количество жителей для данного города')

    country = CountryInfo(loc_dict['address']['country'])

    try:
        print(country.currencies()[0])
    except KeyError:
        print('Ошибка провайдера данных. Невозможно получить валюту для данной страны')


if __name__ == '__main__':
    diploma()
