


def calc(num1 , op , num2):
    op = str(op)
    num1 = int(num1)
    num2 = int(num2)
    if(op == '+'):
        return num1+num2
    elif(op == '-'):
        return num1-num2
    elif(op == '*'):
        return num1*num2
    elif(op == '/'):
        return num1/num2
    else:
        return False
no_done = True

while no_done:
    num1 = input("What is your first number?")
    op = input("What operation d you want. +, -, * . /")
    num2 = input("What is your second number?")
    print(calc(num1 , op , num2))
    
    end = input('Do you want to do other calculations? Y , N')
    if str(end) == 'N':
        no_done = False

