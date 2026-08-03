# Entry point — welcome screen, routes to the main menu and handles user input
from services.auth_service import check_user_present_in_db
from getpass import getpass
from repositories.add_new_account_in_db import add_acc
from services.account_service import balance_inquiry
from services.account_service import deposit_money
from services.account_service import check_requests

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
        user_acc = int(input('''1: Select 1 for login user existing account!!:\n 2: Select 2 for creating new account!: '''))
        if user_acc == 1:
            username = input('Please Enter your username: ')
            password = input(f'''Please Enter your passwrod for {username} account: ''')
            user = check_user_present_in_db(username, password)
            if user != None:
                print(f'Welcome Back, {user['name']}!')
                while True:
                    current_user = user
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
                                8.    Requests
                                9.    Exit

                                =====================================================
                        ''')
                    user_choice = int(input(' Choose an option (1-9): '))
                    match user_choice:
                        case 1:
                            balance = balance_inquiry(current_user)
                            print(f"Your current balance is: {balance['balance']}\n")
                        case 2:
                            account_number = input('Please enter account number where you want to deposit: ')
                            amount = int(input("Please enter amount that you want to desopit: "))
                            request = deposit_money(current_user,account_number, amount)
                            if request['success']: 
                                print(f'Deposite request send successfully to {request['requested_to']}')
                            else:
                                print('User not found with this account number', account_number)
                        case 3:
                            pass
                        case 4:
                            pass
                        case 5:
                            pass
                        case 6:
                            pass
                        case 7:
                            pass
                        case 8:
                            pass
                        case 9:
                            requests = check_requests(current_user)
                            
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