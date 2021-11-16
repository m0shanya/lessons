"""
Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран. Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево
"""

string = str(input("Your string: "))
my_list = list(string)
if my_list[::-1] == my_list:
    print("yes, it is a palindrome")
else:
    print("no, it is not a palindrome")
