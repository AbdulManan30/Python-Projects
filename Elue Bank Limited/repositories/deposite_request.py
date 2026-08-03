from repositories.query_templete import main_func


def check_deposit_from_user_in_db(account_number):
   return main_func(
       """
        SELECT name, phone, id
        FROM users
        WHERE phone = %s
        """, (account_number, )
)

def add_deposit(deposit_from_user, current_user, amount):
    result = main_func(
        """
        INSERT INTO deposit_requests (
            requested_to_id,
            requestor_id,
            requestor_name,
            amount_requested,
            account_number,
            requested_to_name
        )
        VALUES (%s, %s, %s, %s, %s, %s);
        """,
        (
            deposit_from_user["id"],
            current_user["id"],
            current_user["name"],
            amount,
            current_user["phone"],
            deposit_from_user["name"],
        ),
    )
    return{
        'success': True,
        'requested_to': deposit_from_user["name"]
    }

    
def fetch_deposit_req_for_current_user(current_user):
    pass
    
    
    
    
    
    