import unittest
from app import app
from flask_testing import TestCase
import json

class APITestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'test_secret_key'
        return app

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API is running"})

    def test_login(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

    def test_protected_no_token(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()