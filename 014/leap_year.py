year = int(input("Put a year you want to check if its leap or not"))

def is_leap(year):
    is_true = False
    if year % 400 == 0:
        is_true = True
    elif year % 4 == 0 and year %100 != 0:
        is_true = True
    elif year % 4==0 and  year % 100 == 0:
        is_true = False
   
    return is_true
print(is_leap(year))