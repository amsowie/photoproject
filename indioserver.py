import sys
import json
import bcrypt
from flask import (Flask, render_template, jsonify, request, session, redirect,
                   flash)
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import requests
import os
from model import connect_to_db, db, User
app = Flask(__name__)
app.secret_key = "Thanksforallthefish"
app.jinja_env.undefined = StrictUndefined

##############################################################################


@app.route('/')
def index():
    """Indio project homepage displaying public images

    """

    # need way to upload images
    # way to mark image as private for each user
    # unique share link after uploading image
    # need user log in form
    # same url should return same image- .first()???

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    """Login page process user info

    """
    email = request.args.get('email')
    password = request.args.get('pword')
    button = request.args.get('submit')

    user = User.query.filter(User.email == email).first()

    if user and not (bcrypt.hashpw(password.encode('utf-8'),
                     user.password.encode('utf-8')) == user.password):
        flash("A user with that email exists. \
              Please login or choose a different email.")
        return redirect('/')
    elif user:
        session['userid'] = user.user_id
        return redirect('/users/' + str(user.user_id))

    if button == "Register":
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User(email=email, password=hashed_pass)

        db.session.add(user)
        db.session.commit()

        return redirect('/users/' + str(user.user_id))
    else:
        flash("That email doesn't exist. \
              Please register or choose a different email.")
        return redirect('/')

# @app.route('/image/<width>/<height>')
# def special_display():
#     """Display public image with specific dimensions
#     Valid parameters are width >=0 height >=0

#     """
    # return random image with h and w dimensions, or closes sized image
    # same url should always return same image


    #return render_template()


@app.route('/users/<user_id>')
def special_display():
    """Display user link and private images """


    return render_template('user.html', user_id=user.user_id)


##############################################################################
if __name__ == "__main__":  # will connect to db if you run python server.py
    app.debug = True        # won't run in testy.py because it's not server.py
    connect_to_db(app)
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")