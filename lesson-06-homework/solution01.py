"""
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.
"""

"""
попытка написания функции для заменя знаков препинания пробелами

import string
def replace(text):

    for char in text:
        if char in string.punctuation:
            text = text.replace(char, None)

    return text
"""


def two_words(s):
    words = s.split() #разбиение теста на список слов
    i = 0 
    count = 0 #счётчик упоминания слова в списке
    dict = {} #словарь для записи слов и кол-ва их повторения 
    for i in range(len(words)): #цикл для перебора слов в списке
        for id, val in enumerate(words): #цикл для сравнения слов списка
            if words[i] == words[id]: #если найдено повторяющееся слово, то: 
                count += 1
            else: #иначе продолжаем искать
                continue
        dict[words[i]] = count #словарь, в котором ключ - само слово, а значение - кол-во повторений слова
        count = 0 #обнуление счётчика для нового слова
    max_val = max(dict.values()) #поиск наиболее часто встречающегося слова по значению 
    final_dict = {k: v for k, v in dict.items() if v == max_val} #словарь из одного ключа и значения, в котором заключено слово из прошлого действия
    max_word = '' #пусть максимально длинным словом будет вот ЭТО. Тогда:
    for word in words: #цикл для поиска наидлиннейшего слова
        if len(word) > len(max_word): #если слово больше чем ТО
            max_word = word #то найденное слово становится максимально длинным

    print(
        f"Наиболее часто встречающееся слово {final_dict.keys()}. Оно встречается {final_dict.values()} раз.\n"
        f"Самым длинным является слово - {max_word}")
    return


s = str("Hello world and Hello people") #тестовое значение
#s = str(input("Input text:\n\t"))#ввод с клавиатуры
# print(f"Modified string is {replace(s)}")
two_words(s)
