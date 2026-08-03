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
    total_requests = main_func(
        '''
            SELECT  id ,requestor_id, requestor_name, amount_requested, desopit_status, account_number
            FROM deposit_requests
            WHERE requested_to_id = %s
            ORDER BY created_at DESC
        ''', (current_user['id'],), 'all'
        
    )
    return total_requests
    
    
    
def approve_deposit_in_db(current_user, selected_request):
    decrease_balance = main_func(
        """
        UPDATE accounts
        SET balance = balance - %s
        WHERE user_id = %s
        AND balance >= %s
        """,
        (
            selected_request["amount_requested"],
            current_user["id"],
            selected_request["amount_requested"],
        ),
    )

    if not decrease_balance["success"]:
        return "You don't have enough balance to make this deposit."

    increase_balance = main_func(
        """
        UPDATE accounts
        SET balance = balance + %s
        WHERE user_id = %s
        """,
        (
            selected_request["amount_requested"],
            selected_request["requestor_id"],
        ),
    )

    if not increase_balance["success"]:
        return "Something went wrong while crediting the receiver."

    main_func(
        """
        UPDATE deposit_requests
        SET desopit_status = 'Approved'
        WHERE id = %s
        """,
        (selected_request["id"],),
    )

    return "Deposit done successfully."