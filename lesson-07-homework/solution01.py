def check_coords(x1: int, y1: int, x2: int, y2: int) -> bool:
    return (abs(x1-x2) == 1 and abs(y1-y2) == 2) or (abs(y1-y2) == 1 and abs(x1-x2) == 2)
"""
суть решения в том, что конь ходит буквой Г, 
и разница в координатах в таком случае будет 1 по Х и 2 по У(или наоборот).
Исключаются варианты, когда фигуры стоят на одной линии на оси Х/У или по диагонали друг от друга. 
В таких случаях конь не может быит своего тёску.
"""

if __name__ == "__main__":
    while True:
        x1 = int(input("Enter X1:"))
        y1 = int(input("Enter Y1:"))

        x2 = int(input("Enter X2:"))
        y2 = int(input("Enter Y2:"))

        if check_coords(x1, y1, x2, y2):
            print("YES")
        else:
            print("NO")

        c = int(input("Do you want yo continue?(1/2)"))
        if c != 1:
            break


