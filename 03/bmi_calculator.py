weight  = input('What is your weihgt?')
height = input('What is your height in meters?')

bmi = float(weight)/(float(height) ** 2)

#print('your bmi is: ' + str(bmi))
if(bmi<18.5):
    print("You are underweight")

elif(bmi<25):
    print("You are normal weight")

else:
    print("You are overweight")
