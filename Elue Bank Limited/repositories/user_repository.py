# SQL queries for users table
from repositories.query_templete import main_func


def find_user_by_password_and_username(username, password):
    user = main_func(
        """
        SELECT *
        FROM users
        WHERE password = %s AND user_name = %s
        """,
        (password, username),
    )
    return user
