"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну.
Оформить в виде программы, которая считывает название города и выводит на печать страну.
"""


def country(city):
    dict_of_country = {
        "Беларусь": ["Минск", "Витебск", "Могилёв"],
        "Россия": ["Москва", "Лининград", "Кросноярск"],
        "Германия": ["Мюнхен", "Берлин", "Кёльн"],
        "Франция": ["Париж", "Монако", "Марсель"],
    }
    for countr, cities in dict_of_country.items():
        if city in cities:
            return countr


if __name__ == "__main__":
    city = str(input("Input city:\n"))
    print(f"Вы ввели {city}, получаете {country(city)}")
