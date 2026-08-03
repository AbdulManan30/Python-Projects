# Balance, deposit, withdraw, history
from repositories.accounts_repository import check_user_balance
from repositories.deposite_request import add_deposit
from repositories.deposite_request import check_deposit_from_user_in_db
from repositories.deposite_request import fetch_deposit_req_for_current_user

def balance_inquiry(current_user):
    balance = check_user_balance(current_user)
    return balance


def deposit_money(current_user, account_number, amount):
    deposit_from_user = check_deposit_from_user_in_db(account_number)
    if deposit_from_user:
        result = add_deposit(deposit_from_user, current_user, amount)
        return result
    
def check_requests():
       data = fetch_deposit_req_for_current_user()
       print(data)
    
    