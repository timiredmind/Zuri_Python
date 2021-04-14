import time
from random import randint

database = {
    "Seyi": "passwordSeyi",
    "Mike": "passwordMike",
    "Love": "passwordLove"}

account_database = {
    "Seyi": 7245678901,
    "Mike": 6745321908,
    "Love": 8374859402}

account_balance = {
    "Seyi": 0.00,
    "Mike": 0.00,
    "Love": 0.00}


def verify_username():
    if username not in database.keys():
        return False
    return True


def verify_password(password):
    if database[username] == password:
        return True
    return False


def change_password():
    print("Enter your old password")
    password = input()
    if database[username] == password:
        print("Enter your new password: ")
        new_password1 = input()
        print("Enter your new password again")
        new_password2 = input()
        if new_password1 == new_password2:
            database[username] = new_password1
            print("Your new password has been set")
        else:
            print("...Passwords do not match...")
            print("Failed to set new password")
    else:
        print("Invalid password entered")


def generate_account(username):
    account_num = []
    while True:
        for num in range(10):
            number = str(randint(1, 9))
            account_num.append(number)

        account_number = int("".join(account_num))
        if account_number in account_database.values():
            continue
        else:
            account_database[username] = account_number
            return account_number


def register():
    print("Enter your name: ")
    name = input("").capitalize()
    while not name.isalpha():
        print("Name should contain only letters")
        print("Enter your name below: ")
        name = input().capitalize()
    password = "password" + name
    database[name] = password
    account_balance[name] = 0.00
    generate_account(name)
    time.sleep(4)
    print("...Your registration is complete...")
    print(f"Your username is {name}")
    print(f"Your password is {password}")


def login():
    print("What is your name? ")
    global username
    username = input().capitalize()
    if verify_username() is False:
        print("Invalid username")
        print("Would you like to open an account with us? Enter 'yes'/'no': ")
        answer = input().lower()
        if answer == "yes":
            register()
            if login:
                return True
        else:
            return False
    else:
        count = 3
        print("Enter your password: ")
        password = input()
        if verify_password(password) is False:
            for x in range(count):
                attempt = count - x
                print("Wrong password entered")
                print(
                    f"Enter your password: (You have {attempt} attempt left) ")
                password = input()
                if verify_password(password):
                    break
                elif attempt == 1 and verify_password(password) is False:
                    return "Blocked"
            print(f"Welcome {username}")
            return True
        return True


def bankOperation():
    a = login()
    if a is True:
        while True:
            print("These are the available options")
            print("1. Withdrawal")
            print("2. Cash Deposit")
            print("3. Complaint")
            print("4. View account balance")
            print("5. Change password")
            print("6. Display account number")

            print("Please select an option:")
            selectedOption = int(input())
            while selectedOption not in range(1, 7):
                print("Invalid Option Selected, Try again")
                selectedOption = int(input())

            if selectedOption == 1:
                print("How much would you like to withdraw ")
                amount = float(input())
                if account_balance[username] > 0:
                    amount = min(amount, account_balance[username])
                    account_balance[username] -= amount
                    time.sleep(2)  # Delays the output for 2 seconds
                    print("Take your cash")
                else:
                    print("Insufficient balance")

            elif selectedOption == 2:
                print("How much would you like to deposit?")
                deposit = float(input())
                account_balance[username] += deposit
                print(
                    f"Your current balance is {account_balance[username]} naira")

            elif selectedOption == 3:
                print("What issue will you like to report?")
                complaint = input()
                print("Thank you for contacting us.")

            elif selectedOption == 4:
                print(
                    "Your account number is %.2f" %
                    account_balance[username])

            elif selectedOption == 5:
                change_password()

            else:
                print(f"Your account number is {account_database[username]}")

            print("Would you like to continue:  Enter 'yes'/'no' ")
            response = input().lower()
            if response == 'yes':
                continue
            else:
                print("Thank you, You can take your card1")
                break

    elif a == "Blocked":
        print("Take you card, your account has been deactivated. Visit your nearest bank to re-activate")

    else:
        print("Thank you You can take your card")


if __name__ == "__main__":
    bankOperation()
