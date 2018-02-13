from flask import Flask
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text

db = SQLAlchemy()

# ##############################################################################
# Model definitions


class User(db.Model):
    """User data to store after login"""

    __tablename__ = "users"

    #u_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), primary_key=True,
                          server_default=sa_text("uuid_generate_v4()"))
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):  # pragma: no cover
        """Useful printout of user object"""

        return "<User user_id={} email={}>".format(self.user_id, self.email)

##############################################################################


def example_data():
    """Test data samples for tests.py file to use in database"""

    user1 = User(email="bb@bb.com",
                 password=bcrypt.hashpw('bestie', bcrypt.gensalt()))
    user2 = User(email="kb@kb.com",
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

    from indioserver import app

    connect_to_db(app)
    db.create_all()
    print "Connected to DB."
