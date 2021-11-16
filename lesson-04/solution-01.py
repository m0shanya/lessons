"""
Дан список my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], выведите все элементы, которые меньше 5.
"""

my_list_1 = []
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in my_list:
    if x < 5:
        my_list_1.append(x)
print("Result is:", my_list_1)
