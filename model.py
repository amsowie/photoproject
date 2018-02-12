from flask import Flask
import bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ##############################################################################
# Model definitions

class User(db.Model):
    """User data to store after login"""

    __tablename__ = "users"

    u_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    #unique = 

    def __repr__(self):  # pragma: no cover
        """Useful printout of user object"""

        return "<User user_id={} fname={} lname={} email={}>".format(self.u_id,
                                                                     self.fname,
                                                                     self.lname,
                                                                     self.email)

##############################################################################


def example_data():
    """Test data samples for tests.py file to use in database"""

    user1 = User(fname='Brian', lname='Beaman', email="bb@bb.com",
                 password=bcrypt.hashpw('bestie', bcrypt.gensalt()))
    user2 = User(fname='Kari', lname='Baldwin', email="kb@kb.com",
                 password=bcrypt.hashpw('friendly', bcrypt.gensalt()))

    db.session.add_all([user1, user2])
    db.session.commit()


def connect_to_db(app, db_uri='postgresql:///photo_share'):
    """Connect the database to our Flask app."""

    # Configure to use our PostgresSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)  
    print "Connected to DB."
