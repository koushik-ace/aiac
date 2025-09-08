import os
import json
import hashlib

DATA_FILE = "users.json"

# Hardcoded users (username: password)
HARDCODED_USERS = {
    "admin": "admin123",
    "guest": "guestpass"
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)

def register(users):
    username = input("Enter a new username: ")
    if username in users or username in HARDCODED_USERS:
        print("Username already exists.")
        return
    password = input("Enter a new password: ")
    users[username] = hash_password(password)
    save_users(users)
    print("Registration successful.")

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Check hardcoded users (plain-text)
    if username in HARDCODED_USERS and HARDCODED_USERS[username] == password:
        print("Login successful! (hardcoded user)")
        return
    # Check stored users (encrypted)
    if users.get(username) == hash_password(password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    users = load_users()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
