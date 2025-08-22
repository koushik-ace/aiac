def Age_Classifies():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Invalid age entered.")
        elif age <= 12:
            print("You are classified as: child")
        elif age <= 19:
            print("You are classified as: teen")
        elif age <= 59:
            print("You are classified as: adult")
        else:
            print("You are classified as: senior")
    except ValueError:
        print("Please enter a valid integer for age.")

# Example usage
Age_Classifies()