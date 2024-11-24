from flask import render_template, request
from datetime import datetime, timedelta
from helper import apology
import cgecko
from database import db
from helper import *
from currencies import get_coin_from_db_by_id

# class crypto_coin(object):
#     def __init__(self, id, icon_url, symbol, name, quantity, price, current_price):
#         self.id = id
#         self.icon_url = icon_url
#         self.symbol = symbol
#         self.name = name
#         self.quantity = quantity
#         self.price = price
#         self.current_price = current_price

#     def __str__(self):
#         return (f"Crypto Coin [ID: {self.id}, Symbol: {self.symbol}, Name: {self.name}, "
#                 f"Quantity: {self.quantity}, Purchase Price: ${self.price:.2f}, "
#                 f"Current Price: ${self.current_price:.2f}]")


def details():
    coin_id = validate_int_positive(request.args.get("id"), "CoinID")
    if not validate_id_in_table("currencies", coin_id, "id"):
        return apology("Error finding the coin.\nplease try again.", 404)
    coin = get_coin_from_db_by_id(coin_id)[0]
    return render_template("coin_details.html", coin=coin)