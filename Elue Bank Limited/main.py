# Entry point — welcome screen, routes to the main menu and handles user input
from services.auth_service import check_user_present_in_db
from getpass import getpass
from repositories.add_new_account_in_db import add_acc

def main():
    current_user = None

    def new_user_creation():
        print("=" * 40)
        print("      CREATE NEW ACCOUNT")
        print("=" * 40)

        name = input("Enter Full Name       : ").strip()
        username = input("Enter Username        : ").strip()
        phone = input("Enter Phone Number    : ").strip()
        email = input("Enter Email           : ").strip()

        while True:
            password = getpass("Create Password      : ")
            confirm_password = getpass("Confirm Password     : ")

            if password == confirm_password:
                break

            print("Passwords do not match. Please try again.\n")

        return {
            "name": name,
            "username": username,
            "phone": phone,
            "email": email,
            "password": password
        }
    while True:
        print('Welcome to Elue Bank limited: ')
        user_acc = int(input('''1: Select 1 for login user existing account!!:
        2: Select 2 for creating new account!: '''))
        if user_acc == 1:
            username = input('Please Enter your username: ')
            password = input(f'''Please Enter your passwrod for {username} account: ''')
            user = check_user_present_in_db(username, password)
            print(user)
            if user != None:
                current_user = user
                print(f'Welcome Back, {current_user['name']}!')
                print('''
                            =====================================================
                                            MAIN MENU
                            =====================================================

                            1. 💰 Balance Inquiry
                            2. 💵 Deposit Money
                            3. 💸 Withdraw Money
                            4. 📜 Transaction History
                            5. 🔐 Change Password
                            6. 👤 Account Information
                            7. 🚪 Logout
                            8.    Exit

                            =====================================================
                      ''')
                user_choice = int(input(' Choose an option (1-8): '))
                if user_choice == 8:
                    break
            else:
                print('Sorry User not found')
                break
       
        elif user_acc == 2:
            user_info = new_user_creation()
            if add_acc(user_info)['success']:
                print('Your account has been created now you can login your account!')
            else:
                print('Failed: user already exist in database')
main()