age = input("What is your age")

def weeks(age):
    age_left = 52*(90-int(age))
    age_lived = int(age)*52
    print(f"Weeks lived: {age_lived} weeks lived")
    print(f"You have: {round(age_left)} weeks left")

weeks(age)