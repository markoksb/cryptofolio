from flask import render_template
from datetime import datetime, timedelta
from helper import apology
import cgecko
from database import db


def details():
    return render_template("coin_details.html")