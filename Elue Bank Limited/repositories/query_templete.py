from database.db_connection import get_connection
from psycopg2.extras import RealDictCursor
def main_func(query, data_tuple=(), fetch_type='one'):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cursor.execute(query, data_tuple)

        if cursor.description:
            if fetch_type == 'one':
                data = cursor.fetchone()
            elif fetch_type == 'all':
                data = cursor.fetchall()
            conn.commit()      # <-- commit before return
            return data

        conn.commit()
        return {"success": True}

    except Exception as e:
        conn.rollback()
        return {
            "success": False,
            "error": str(e)
        }

    finally:
        cursor.close()
        conn.close()
