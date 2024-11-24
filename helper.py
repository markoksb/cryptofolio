from flask import render_template, redirect, session
from functools import wraps
from database import db

def validate_float_positive(value, name: str):
    """Validate value to be a positive number"""
    try:
        val = float(value)
        if val < 0:
            raise ValueError(f"{name} must be positive.")
        return val
    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)
    

def validate_int_positive(value, name: str):
    """Validate value to be a positive integer"""
    try:
        val = int(value)
        if val < 0:
            raise ValueError(f"{name} must be positive.")
        return val
    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)


def validate_id_in_table(table_name: str, id_value: int, id_name: str = "id") -> bool:
    """Check if an ID exists in the specified table."""
    return db.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {id_name} == ?", id_value)[0]["COUNT(*)"] == 1


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("error.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function
