from flask import redirect, session, render_template
from functools import wraps

def login_required(f):
    """ Decorate routes to require login. """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/welcome")
        return f(*args, **kwargs)
    
    return decorated_function

def apology(page, message, code=400):
    """ Render message to user. """
    return render_template(page, message=message), code