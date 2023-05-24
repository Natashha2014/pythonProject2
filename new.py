# 1. Create a string using all capital letters and invoke the method that would make all letters lowercase.
# 2. Create a string using all lowercase letters and invoke the method that would make all letters uppercase.
# 3. Create a list with 10 elements and change the 4th element.
# 4. Add a new element after the 3rd element.
# 5. Add 2 elements to the end of the list.
# 6. Remove the first element.
# 7. Delete the 6th element
# 8. Create a dictionary with following keys - FirstName, LastName, Age, Height.
# 9. Update the values of Age and Height.
# 10. Write a code that would check for following conditions

name = "ANANO"
print(name.lower())
name = "anano"
print(name.upper())
items = ["Farook", "Elene", "Academy", 100, 8, "Natia", 11.5, 23, "Gagi", "Naseem"]
print(items)
items[4] = "tojtech"
print(items)
items.insert(4, "Bootcamp")
items.append("Skhvitaridze" " 1000")
print(items)
items.remove("Farook")
print(items)
del items[6]
print(items)
dictionary = {"FirstName": "Ana", "LastName": "Skhvitaridze", "Age": 32, "Height": 162}
print(dictionary)
new_dictionary = {"Age": 33}
new_dictionary = {"Height": 163}
dictionary.update(new_dictionary)
print(dictionary)