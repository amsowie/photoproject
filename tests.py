from unittest import TestCase
import bcrypt
import json
from flask import jsonify
from indioserver import app
from model import connect_to_db, db, example_data


class FlaskTests(TestCase):

    def setUp(self):
        """Set this up before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True  # shows debugging output
        connect_to_db(app, "postgresql:///testdb")
        app.config['SECRET_KEY'] = 'key'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_name'] = 'Brian'
                sess['user_id'] = 1

        #create tables and ad sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Clear database at end of test"""

        db.session.close()
        db.drop_all()  # get rid of fake data

    def test_index(self):
            """Test the homepage route"""

            result = self.client.get("/")
            self.assertEqual(result.status_code, 200)
            self.assertIn('Welcome', result.data)  


    def test_user_login(self):
        """Test user page is visible with session"""

        #test correct password, successful login
        result = self.client.post("/login", data={'email': 'bb@bb.com',
                                                  'password': 'bestie'},
                                                   follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("Welcome,", result.data)

        # test incorrect password
        result = self.client.post("/login", data={'email': 'bb@bb.com',
                                                  'password': 'fail'},
                                                   follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("Password incorrect.", result.data)

        # test no user, redirect to registration page
        result = self.client.post("/login", data={'email': 'no@user',
                                                  'password': 'fail'},
                                                   follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("No user", result.data)

##############################################################################

if __name__ == "__main__":
    import unittest
    unittest.main()
