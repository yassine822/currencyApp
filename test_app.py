import unittest
from app import app   # import your Flask app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        # Check if homepage ("/") loads successfully
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Currency Converter", response.data)  # match your index.html title

    def test_converter_page(self):
        # Check if converter page loads
        response = self.app.get('/calculator')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
