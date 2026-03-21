print("Welcome to the tip calculator!")

bill = input("What is your total bill?")
tip =  input("What procentage tip would you like to give? 10, 12 or 15?")
ppl = input("How many people split the bill?")

total = float(bill) +float(tip)/100*float(bill)
total_per_person = round(total/int(ppl) , 2) 

print("Everyone , should pay : " + "$"+str(total_per_person))
