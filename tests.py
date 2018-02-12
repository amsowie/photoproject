from unittest import TestCase
import doctest
import bcrypt
import json
from flask import jsonify
from indioserver import app
# from model import connect_to_db, db, example_data


class FlaskTests(TestCase):

    def setUp(self):
        """Set this up before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True  # shows debugging output

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_name'] = 'Brian'
                sess['user_id'] = 1


    def test_index(self):
            """Test the homepage route"""

            result = self.client.get("/")
            self.assertEqual(result.status_code, 200)
            self.assertIn('Welcome', result.data)  # getting the data string back

##############################################################################

if __name__ == "__main__":
    import unittest
    unittest.main()
