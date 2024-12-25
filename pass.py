import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("enter your username: ")
    password = getpass.getpass("enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Accout creation success!")

def logIn():
    username = input("enter your username: ")
    password = getpass.getpass("enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login success!")
    else: 
        print("Invalid username or password.")
    
def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            logIn()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()