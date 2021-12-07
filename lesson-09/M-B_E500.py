"""
Создать программу, которая импортирует класс из предыдущей задачи,
создает объект и при инициализации устанавливает марку Mercedes, модель E500, год выпуска 2000.
Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""

from class_car import Car
from class_car import game


def solution(my_car):
    while my_car.speed < 100:
        my_car.speed_plus()
    my_car.now_speed()
    return


if __name__ == "__main__":
    c = 0
    car = Car("Mercedes-Benz", "E500 ", 2000, 0)
    print("Brand: ", car.brand)
    print("Model: ", car.model)
    print("Year: ", car.year)
    print(f"Start speed: {car.speed}\n")
    print("game(0) or solution(1)? ")
    choice = int(input())
    if choice == 0:
        game(car)
    else:
        solution(car)
