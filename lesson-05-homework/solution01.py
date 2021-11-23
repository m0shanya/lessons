"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.  
В результате ее работы на печать выводятся значения переданных переменных, но только если они не равны None. 
Получим, например, следующее сообщение: Переданы аргументы: var1 = 2, var3 = 10.
"""
def three_args(spis):
    j = 1
    for i in spis:
        if i != None:
            print(f"elements passed:\nvar{j} = {i}")
            j += 1
    return


a = int(input("Input any number:\n"))
b = int(input("Input any number:\n"))
c = int(input("Input any number:\n"))
spis = []
spis.append(a)
spis.append(b)
spis.append(c)
three_args(spis)