def month_to_season(num):
    winter = [1, 2, 12]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    vesna = [9, 10, 11]
    if num in winter: print("Winter")
    elif num in spring: print("Spring")
    elif num in summer: print("Summer")
    elif num in vesna: print("Vesna")
    return

num = int(input("Number of month: "))
"""
while num:
    if (num < 1) and (num > 12):
   
print("Input numbers 1 - 12")
num = int(input("Number of month: "))
"""
month_to_season(num)
