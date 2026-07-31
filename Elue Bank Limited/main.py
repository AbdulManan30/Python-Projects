# Entry point — welcome screen, routes to the main menu and handles user input
from services.auth_service import check_user_present_in_db

def main():
    current_user = None
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
                if int(input(' Choose an option (1-8): ')) == 8:
                    break
main()