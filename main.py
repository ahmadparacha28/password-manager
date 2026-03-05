import pyperclip
import re
from password_generator import generate_password
from database import connect, insert_data, view_data
from encryption import encrypt_password, decrypt_password

connect()  # This will create the database and table if not exists

def check_strength(password):
    if len(password) < 8:
        return "Weak: less than 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Weak: no uppercase letters"
    if not re.search(r"[a-z]", password):
        return "Weak: no lowercase letters"
    if not re.search(r"[0-9]", password):
        return "Weak: no digits"
    if not re.search(r"[!@#$%^&*()]", password):
        return "Weak: no special characters"
    return "Strong"

def show_menu():
    print("\n==== Password Manager ====")
    print("1. Add New Password")
    print("2. View Saved Passwords")
    print("3. Generate Password")
    print("4. Exit")


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        website = input("Enter website: ")
        username = input("Enter username: ")


        print("1. Enter my own password")
        print("2. Generate a secure password")
        pwd_choice = input("Choose option: ")

        if pwd_choice == "1":
            password = input("Enter password: ")
            strength = check_strength(password)
            print("Password Strength:", strength)
        elif pwd_choice == "2":
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print("Generated Password:", password)
        else:
            print("Invalid option, using default password length 12.")
            password = generate_password(12)
            print("Generated Password:", password)

        encrypted = encrypt_password(password)
        insert_data(website, username, encrypted)
        print("Password saved successfully!")

    elif choice == "2":
        rows = view_data()
        if not rows:
            print("No passwords saved yet.")
        else:
            for row in rows:
                decrypted = decrypt_password(row[3])
                print(f"ID: {row[0]}, Website: {row[1]}, Username: {row[2]}, Password: {decrypted}")
            copy_id = input("Enter ID of password to copy to clipboard (or press Enter to skip): ")
            if copy_id:
                copy_id = int(copy_id)
                for row in rows:
                    if row[0] == copy_id:
                        pyperclip.copy(decrypt_password(row[3]))
                        print("Password copied to clipboard!")
    
    elif choice == "3":
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Generated Password:", password)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")


