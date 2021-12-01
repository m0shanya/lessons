from func import filter_cars


if __name__ == "__main__":
    car_list = [
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
    year = int(input("Input year: "))
    # res = filter_cars(car_list, year)
    # print(res)
    print(list(filter(lambda x: x["year"] < year, car_list)))
