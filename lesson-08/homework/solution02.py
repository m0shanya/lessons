"""
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу
и что это за элемент.
Т.е. если программе на вход подать последовательность [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5],
то на печать программа должна вывести числа 4 и 3, где 4 - повторяющийся элемент, 3 - количество повторений
"""


def normalization(spisok: list) -> list:
    flag_0 = 0
    flag_1 = 0
    my = []
    for i in range(0, len(spisok)):
        if spisok[i] == 0:
            flag_0 = i
        for j in range(flag_0, len(spisok)):
            if spisok[j] == 0:
                flag_1 = j
    if flag_0 < flag_1:
        for k in range(0, flag_1 + 1):
            my.append(spisok[k])
    else:
        for k in range(0, flag_0):
            my.append(spisok[k])
    return my


def counting(numbers: list) -> dict:
    count = 0
    my_dict = {}
    for n in range(0, len(numbers)):
        for m in range(n + 1, len(numbers)):
            if numbers[m] != numbers[n]:
                break
            elif numbers[m] == numbers[n]:
                count += 1
        my_dict[numbers[n]] = count
    return my_dict


my_list = [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5]
a = normalization(my_list)
print(f"transformed list is {a}")
b = counting(a)
print("list was transformed in dictionary({number: number of repetitions}) ", b)
max_value = max(b.values())
final_dict = {k: v for k, v in b.items() if v == max_value}
print("{number: number of repetitions} - ", final_dict)