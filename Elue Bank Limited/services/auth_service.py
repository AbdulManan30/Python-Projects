# Login, PIN verification, lockouts
from repositories.user_repository import find_user_by_password_and_username

def check_user_present_in_db(username, password):
    result = find_user_by_password_and_username(username, password)
    if result:
        return result
    return None