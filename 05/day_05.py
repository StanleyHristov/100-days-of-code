import string 
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

lenght = int(input("How long do you want your password to be?"))

new_list = []
for i in range(0 , round(lenght/3)):
    new_list += random.choice(letters)
    new_list += random.choice(numbers)
    new_list += random.choice(symbols)

print("".join(new_list))


