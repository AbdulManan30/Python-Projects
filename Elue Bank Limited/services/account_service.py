# Balance, deposit, withdraw, history
from repositories.accounts_repository import check_user_balance
def balance_inquiry(current_user):
    balance = check_user_balance(current_user)
    return balance
    