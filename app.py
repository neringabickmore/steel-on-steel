import os
from flask import(
   Flask, render_template)


if os.path.exists("env.py"):
    import env

APP = Flask(__name__)

APP.secret_key = os.environ.get("SECRET_KEY")
APP.env = os.environ.get("DEBUG")


@APP.route("/")
def about():
    """
    About page route.
    """
    return render_template("pages/about.html")


if __name__ == "__main__":
    APP.run(
        host=os.environ.get("IP"),
        port=os.environ.get("PORT"),
        debug=os.environ.get("DEBUG"))