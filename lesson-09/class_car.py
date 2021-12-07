"""
Создать класс Car.
Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задния ход (изменение знака скорости).
"""


class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def speed_plus(self):
        self.speed += 5
        print(f"increased speed is {self.speed}")

    def speed_minus(self):
        self.speed -= 5
        print(f"reduced speed is {self.speed}")

    def speed_null(self):
        self.speed = 0
        print("speed is null")

    def now_speed(self):
        print(f"now speed {self.speed}")

    def revers(self):
        self.speed = -self.speed
        print(f"R: {self.speed}")


def game(name):  # for fun))))
    c = 0
    while True:
        print(
            "\t\taccelerate the car - 1 || reduce speed - 2 || stop the car - 3 || "
            "задния ход (изменение знака скорости) - 4 || now speed - 5"
        )
        i = int(input())
        if i < 1 or i > 5:
            i = int(input("input numbers 1..5\t"))
        if i == 1:
            name.speed_plus()
        elif i == 2:
            name.speed_minus()
        elif i == 3:
            name.speed_null()
        elif i == 4:
            name.revers()
        elif i == 5:
            print("\n" * 5)
            name.now_speed()
            print("1 - exit || 2 - continue")
            c = int(input())
        if c == 1:
            break


if __name__ == "__main__":
    c = 0
    car = Car("Volkswagen", "Golf Mk.7 GTI ", 2013, 0)
    print(car.brand)
    print(car.model)
    print(car.year)
    print(car.speed)

    game(car)
