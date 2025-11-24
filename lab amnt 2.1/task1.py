def is_valid_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c != ' ')
    # Check if cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if is_valid_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")