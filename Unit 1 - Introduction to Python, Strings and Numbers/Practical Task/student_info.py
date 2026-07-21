# Student Info Formatter
# This program collects a student's first name, surname, age, and favourite number,
# then formats and displays the information in various ways.

first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

print(f"Welcome, {first_name} {surname}!")
print(f"Name in UPPERCASE: {first_name.upper()} {surname.upper()}")
print(f"Name in Title Case: {first_name.title()} {surname.title()}")
print(f"Age in months: {age * 12}")
print(f"Favourite number rounded to 2 decimal places: {round(favourite_number, 2)}")
print(f"Data type of first name: {type(first_name)}")
print(f"Data type of surname: {type(surname)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of favourite number: {type(favourite_number)}")