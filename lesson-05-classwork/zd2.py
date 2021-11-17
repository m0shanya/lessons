import random

def fun(my_spis):
    res_list = []
    sum = 0
    my_spis.sort()
    a = my_spis[-1]
    res_list.append(a)
    for x in my_spis:
        sum += x
    res_list.append(sum)
    return res_list


my_spis = []
for element in range(random.randint(0, 10)): #random.randint(0, 10)
    my_spis.append(element)
print(my_spis)
res_list = fun(my_spis)
print("Max element:", res_list[0])
print("Sum of elements:", res_list[1])
