print("Welcome to python pizza delivery!")
size = input("What size pizza do you want? S , M or L?")
peperoni = input("Do you want peperoni on your pizza? Y or N?")
extra_cheeze = input("Do you want extra cheese on your pizza? Y or N?")
bill = 0

if(size == 'S'):
    bill += 15
elif(size == 'M'):
    bill += 20
elif(size == 'L'):
    bill+=25

if(peperoni =='Y' and size == 'S'):
        bill+=2
elif(peperoni =='Y'):
     bill+=3

if(extra_cheeze == 'Y'):
     bill+=1

print("Your total is: $"+str(bill))
