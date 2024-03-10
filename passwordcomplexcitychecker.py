import re

def check_length(password):
    return len(password) >= 8

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special_char(password):
    special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    return bool(special_chars.search(password))

def assess_password_strength(password):
    checks = [
        ("Length", check_length(password)),
        ("Lowercase", check_lowercase(password)),
        ("Uppercase", check_uppercase(password)),
        ("Digit", check_digit(password)),
        ("Special Character", check_special_char(password))
    ]

    strength = sum(int(check) for _, check in checks)
    feedback = "Weak"

    if strength >= 4:
        feedback = "Strong"
    elif strength >= 3:
        feedback = "Moderate"
    elif strength >= 2:
        feedback = "Weak"

    return feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = assess_password_strength(password)
    print("Password strength:", strength)
