# SQL queries for transactions table
from repositories.query_templete import main_func

def add_transaction_history_in_db(current_user, type, amount):
    current_account_id = main_func(
        """
        SELECT id FROM accounts
        WHERE user_id = %s
        """,
        (current_user['id'],)
    )
    print(current_account_id)
    insert_data = main_func(
        '''
        INSERT INTO transactions (account_id, type, amount)
        VALUES (%s, %s,%s)
        ''',(current_account_id['id'], type, amount)
    )
    if insert_data['success']:
        return 'Done'
    else:
        return 'Not Done'
    
    
    
    
def fetch_all_transaction_from_db(current_user):
    current_account_id = main_func(
        """
        SELECT id FROM accounts
        WHERE user_id = %s
        """,
        (current_user['id'],)
    )
    all_transaction = main_func(
        """
        SELECT * FROM transactions
        WHERE account_id = %s
        """,
        (current_account_id['id'],), 'all'
    )
    return all_transaction