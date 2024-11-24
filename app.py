from flask import Flask, redirect, render_template
from flask_session import Session

import users, currencies, portfolio, coin
from helper import apology

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_NAME"] = "cportfolio"
app.session_cookie_name = "cportfolio"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.add_url_rule("/register", view_func=users.register, methods=["GET", "POST"])
app.add_url_rule("/login", view_func=users.login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=users.logout)
app.add_url_rule("/currencies", view_func=currencies.overview)
app.add_url_rule("/coin_detail", view_func=coin.details)
app.add_url_rule("/portfolio", view_func=portfolio.portfolio)
app.add_url_rule("/create_portfolio", view_func=portfolio.create, methods=["GET", "POST"])
app.add_url_rule("/delete_portfolio", view_func=portfolio.delete, methods=["GET", "POST"])
app.add_url_rule("/coin_add", view_func=portfolio.add_coin_to_portfolio, methods=["GET", "POST"])
app.add_url_rule("/coin_rem", view_func=portfolio.rem_coin_from_portfolio, methods=["GET", "POST"])
app.add_url_rule("/transaction_remove", view_func=portfolio.rem_transaction, methods=["GET"])


@app.route("/")
def index():
    """Home route"""
    return redirect("/currencies")


@app.route("/imprint")
def imprint():
    """Home route"""
    return render_template("imprint.html")


@app.errorhandler(Exception)
def handle_exception(e):
    if hasattr(e, "code"):
        return apology(f"Error: {str(e)}", e.code)
    else:
        return apology(f"Error: {str(e)}", 500)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
