age_input = input("Enter the age: ")
if not age_input.isdigit() or int(age_input) < 0:
    print("Error: Please enter a valid non-negative integer for age.")
else:
    age = int(age_input)
    if age < 12:
        category = "Child"
    if 12 <= age < 19:
        category = "Teen"
    if 19 <= age < 59:
        category = "Adult"
    if age >= 59:
        category = "Senior"
    print("Category:", category)