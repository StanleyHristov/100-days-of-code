import random

user_choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper 2 for scissors "))
if(user_choice == 0):
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
          """)

elif(user_choice == 1):
    print(""" 
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
elif(user_choice == 2):
    print("""
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
           """)
    
c_choice = random.randint(0,2)
if(c_choice ==0):
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
          """)

elif(c_choice == 1):
    print(""" 
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
elif(c_choice == 2):
    print("""
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
           """)
    
if(user_choice == c_choice):
    print("It's a Draw")

elif(user_choice == 0 and c_choice == 2):
    print("You win")
elif(user_choice == 1 and c_choice == 0):
    print("You win")
elif(user_choice == 2 and c_choice == 1):
    print("You win")


elif(c_choice == 0 and user_choice == 2):
    print("You lost")
elif(c_choice == 1 and user_choice == 0):
    print("You lost")
elif(c_choice == 2 and user_choice == 1):
    print("You lost")