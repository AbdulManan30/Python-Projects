from repositories.query_templete import main_func


def check_user_balance(current_user):
    return main_func(
        """
                SELECT balance
                FROM accounts
                WHERE user_id = %s
        """,
        (current_user["id"],),
    )


def withdraw_money_from_db(user, amount_to_withdraw):
    return main_func(
        """
        UPDATE accounts
        SET balance = balance - %s
        WHERE user_id = %s
        AND balance >= %s
        """,
        (amount_to_withdraw, user["id"], amount_to_withdraw),
    )


def update_pass_in_db(current_user, current_pass, new_pass):
    user = main_func(
        """
        SELECT id
        FROM users
        WHERE id = %s AND password = %s
        """,
        (current_user["id"], current_pass),
    )

    if not user:
        return "Current password is incorrect."

    result = main_func(
        """
        UPDATE users
        SET password = %s
        WHERE id = %s
        """,
        (new_pass, current_user["id"]),
    )

    if result["success"]:
        return "Password updated successfully."
    else:
        return "Failed to update password."
