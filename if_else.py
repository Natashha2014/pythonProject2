
age = 21
height = 6.0
time = 10
if age > 21 and height >= 6.0 and time > 10:
    print("You can enter the club")
elif age < 21 and height >= 6.0 and time > 10:
    print("the time of entry and height match the entry criteria but age does not. you are not allowed enter the club")
elif age >= 21 and height < 6.0 and time > 10:
    print("Your age and time of entry match the criteria, but height does not ")
elif age >= 21 and height > 6.0 and time < 10:
    print("Your age and height meet the entry criteria, however you should come back when it’s 10pm")
else:
    print("None of the requirements for entry are met.")

