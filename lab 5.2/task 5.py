def greet_user(name, gender):
    gender = gender.lower()
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    else:
        title = ""
    if title:
        return f"Hello, {title} {name}! Welcome."
    else:
        return f"Hello, {name}! Welcome."

# Example usage:
print(greet_user("Alex", "male"))
print(greet_user("Taylor", "female"))
print(greet_user("Jordan", "non-binary"))
