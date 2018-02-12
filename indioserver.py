import sys
import json
import bcrypt
from flask import Flask, render_template, jsonify, request, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
import requests
import os
app = Flask(__name__)
app.secret_key = "Ahahahahahha!!!!!!"
##############################################################################


@app.route('/')
def index():
    """Indio project homepage displaying public images

    """

    # need way to upload images
    # way to mark image as private for each user
    # unique share link after uploading image

    return render_template('index.html')


# @app.route('/image/<width>/<height>')
# def special_display():
#     """Display public image with specific dimensions
#     Valid parameters are width >=0 height >=0

#     """
    # return random image with h and w dimensions, or closes sized image
    # same url should always return same image


    #return render_template()


# @app.route('/private')
# def special_display():
#     """Display private images with specific dimensions"""



#     return render_template()
##############################################################################
if __name__ == "__main__":  # will connect to db if you run python server.py
    app.debug = True        # won't run in testy.py because it's not server.py
    #connect_to_db(app)
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")