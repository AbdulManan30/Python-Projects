import requests

def convertor():
    curr_convertable = str(
        input("Please enter your currency name in capital latters example PKR: ")
    )
    amount = int(input("Please enter your amount that you want to convert: "))
    curr_want_to_convert = str(
        input(
            f"Please enter the currency name in capital latters that you want to convert in {curr_convertable} example: "
        )
    )
    response = requests.get(f"https://v6.exchangerate-api.com/v6/7ef9520653afe22a31a8b518/latest/{curr_convertable}")
    res = response.json()["conversion_rates"][curr_want_to_convert]*amount
    print(res)
    
convertor()