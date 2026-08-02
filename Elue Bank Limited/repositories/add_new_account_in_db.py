from database.db_connection import get_connection
import random


def add_acc(info):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO users (name, user_name, phone, email, password)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
            """,
            (
                info["name"],
                info["username"],
                info["phone"],
                info["email"],
                info["password"]
            )
        )

        user_id = cursor.fetchone()[0]

        # Insert into accounts table
        cursor.execute(
            """
            INSERT INTO accounts (user_id, account_number)
            VALUES (%s, %s);
            """,
            (user_id, info["phone"])
        )

        conn.commit()

        return {
            "success": True,
            "user_id": user_id,
            "account_number": info["phone"]
        }

    except Exception as e:
        conn.rollback()
        return {
            "success": False,
            "error": str(e)
        }

    finally:
        cursor.close()
        conn.close()