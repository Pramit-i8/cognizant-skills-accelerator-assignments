import re

# Input the Password
password = input("Enter a password: ")

# Now Evaluate the Password

# Check length of the password
length_check = len(password) >= 8

# at least one uppercase letter
uppercase_check = any(char.isupper() for char in password)

# at least one lowercase letter
lowercase_check = any(char.islower() for char in password)

# at least one digit
digit_check = any(char.isdigit() for char in password)

# at least one special character
special_char_check = bool(re.search(r'[@#$%^&+=!]', password))

# Initialize score variable
strength_score = 0

# Evaluate the checks and assign score
if length_check:
    strength_score += 2
else:
    print("Your password needs to be at least 8 characters long.")

if uppercase_check:
    strength_score += 2
else:
    print("Your password needs at least one uppercase letter.")

if lowercase_check:
    strength_score += 2
else:
    print("Your password needs at least one lowercase letter.")

if digit_check:
    strength_score += 2
else:
    print("Your password needs at least one digit.")

if special_char_check:
    strength_score += 2
else:
    print("Your password needs at least one special character (@, #, $, etc.).")

# Print the result based on checks
if strength_score == 10:
    print("Your password is strong! 💪")
else:
    print(f"Your password strength score is {strength_score}/10.")