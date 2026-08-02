from database.db_connection import get_connection
from psycopg2.extras import RealDictCursor

def check_user_balance(current_user):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT balance
        FROM accounts
        WHERE user_id = %s
        """,
        (current_user['id'],)
    )
    user = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return user