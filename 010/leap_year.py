year = input("What year you want to check?")

def check(year):
    year = int(year)
    if(year%400 == 0 ):
        return True
    elif(year%4 ==0 and year%100 !=0):
        return True
    else:
        return False
print(check(year))