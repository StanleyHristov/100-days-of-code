num = int(input("Put a number and see if its prime"))

def is_prime(num):
    is_true = True
    for i in range(2 , num):
        if i!= num or i!=1:
            if num %i ==0:
                is_true = False
    print(is_true)

is_prime(num)