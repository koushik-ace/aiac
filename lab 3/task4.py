def register_user(users_db):
    print("=== Register ===")
    username = input("Enter a new username: ").strip()
    if username in users_db:
        print("Username already exists. Please try a different username.")
        return False
    password = input("Enter a new password: ").strip()
    users_db[username] = password
    print("Registration successful!")
    return True

def login_user(users_db):
    print("=== Login ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users_db and users_db[username] == password:
        print("Login successful! Welcome,", username)
        return True
    else:
        print("Invalid username or password.")
        return False

def main():
    users_db = {}
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()
        if choice == "1":
            register_user(users_db)
        elif choice == "2":
            login_user(users_db)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
