import random

correct = random.randint(0,100)

lives =0
diff = input("What diffciculty would you chouse normal or hard?").lower()
if diff =='normal':
    lives += 10
elif diff =='hard':
    lives += 5

while lives !=0:

    print(f"correct:{correct}")
    number = int(input("Try to guess a number?"))
    if number< correct:
        print("Higher")
        lives -=1
        
    elif number > correct:
        print("Lower")
        lives -=1
        
    else:
        print("You guessed it")
        lives = 0
    
    
    
