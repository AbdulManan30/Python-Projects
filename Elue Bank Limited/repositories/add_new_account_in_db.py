from repositories.query_templete import main_func


def add_acc(info):
    user = main_func(
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
            info["password"],
        ),
    )

    user_id = user["id"]

    main_func(
        """
        INSERT INTO accounts (user_id, account_number)
        VALUES (%s, %s);
        """,
        (user_id, info["phone"]),
    )

    return {
        "success": True,
        "user_id": user_id,
        "account_number": info["phone"],
    }
