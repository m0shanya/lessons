CAR_LIST = [
    {
        "seria": 1234,
        "colour": "red",
        "year": 1999
    },
    {
        "seria": 12345,
        "colour": "gray",
        "year": 2002
    },
    {
        "seria": 12345,
        "colour": "blue",
        "year": 2020
    },
]


def filter_cars(year: int) -> list:
    result = []
    for car in CAR_LIST:
        if car["year"] < year:
            result.append(car)
    return result


if __name__ == "__main__":
    year = int(input("Input year: "))
    # res = filter_cars(year)
    # print(res)
    print(list(filter(lambda x: x["year"] < year, CAR_LIST)))
