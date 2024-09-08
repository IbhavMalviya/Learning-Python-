age=input("Please enter your age: ")
age=int(age)
if age<3:
    print("Your ticket is free.")  
elif age>=3 and age<=12:
    print("Your ticket is $10.")
else:
    print("Your ticket is $15.")
