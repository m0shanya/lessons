def fun(my_list):
    for element in my_list:
        print(f"Hello, {element}!")
    return


my_list = []

for x in range(5):
    name = str(input("Input name: "))
    my_list.append(name)

a = fun(my_list)

