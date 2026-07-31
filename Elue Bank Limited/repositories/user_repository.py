# SQL queries for users table
from database.db_connection import get_connection
from psycopg2.extras import RealDictCursor

def find_user_by_password_and_username(username,password):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE password = %s AND user_name = %s
        """,
        (password, username)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user