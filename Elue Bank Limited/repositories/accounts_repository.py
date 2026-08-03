from repositories.query_templete import main_func

def check_user_balance(current_user):
    print(current_user)
    return main_func(
        """
                SELECT balance
                FROM accounts
                WHERE user_id = %s
        """,
        (current_user["id"],)
    )
