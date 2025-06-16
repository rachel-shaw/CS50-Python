"""
GOALS:
- implement a program that expects the user to specify as a command-line argument the number of bitcoins, n, they want to buy
- if that argument cannot be converted to a float, the program should exit via sys.exit with an error message
- queries the API for the coincap bitcoin price
- 

Website: rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey (replace YourApiKey with key below)
API Key: 798692c6308c9f75b1078b4505365a991d55454e56cfbe288f55543b1b5bfedb
"""

# import sys
# import requests

# def main():

#     if len(sys.argv) == 2:
#         userinput = (sys.argv[1])

#         try:
#             n = float(userinput)
#             try:
#                 response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=798692c6308c9f75b1078b4505365a991d55454e56cfbe288f55543b1b5bfedb")
#             except requests.RequestException:
#                 print("Couldn't complete API request")
#                 return
#         except ValueError:
#             print("Command-line argument is not a number")
#             return
#     elif len(sys.argv) < 2:
#         sys.exit("Missing command-line argument") 
#     else:
#         sys.exit("Too many arguments")
    
#     # print(response.json())
#     print("Searching CoinCap for Bitcoin price")
#     content = response.json()
#     price = content["data"]["priceUsd"]
#     price_total = float(price) * float(n)
#     print(f"- ${float(price_total):,.4f}")

# main()

import sys
import requests

API_URL = "https://rest.coincap.io/v3/assets/bitcoin"
API_KEY = "798692c6308c9f75b1078b4505365a991d55454e56cfbe288f55543b1b5bfedb"

def get_bitcoin_price():
    try:
        response = requests.get(f"{API_URL}?apiKey={API_KEY}")
        response.raise_for_status()
        return float(response.json()["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error: Could not fetch Bitcoin price.")

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price = get_bitcoin_price()
    total_cost = price * num_bitcoins
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
