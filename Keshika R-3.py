import random
import string

length = int(input("Enter password length: "))

if length < 4:
    print("Please enter length of at least 4!")
else:
    characters = ""

    upper = input("Include Uppercase letters (yes/no): ")
    lower = input("Include Lowercase letters (yes/no): ")
    digits = input("Include Numbers     (yes/no): ")
    symbols = input("Include Symbols     (yes/no): ")

    if upper == "yes":
        characters += string.ascii_uppercase
    if lower == "yes":
        characters += string.ascii_lowercase
    if digits == "yes":
        characters += string.digits
    if symbols == "yes":
        characters += string.punctuation

    if characters == "":
        print("Please select at least one character set!")
    else:
        password = ""
        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)
        print("Password Length   :", length)