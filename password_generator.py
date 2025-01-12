```python
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("You must select at least one character type!")
    
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
