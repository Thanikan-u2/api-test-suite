import unittest
import requests

# Use a public dummy API for safety
BASE_URL = "https://jsonplaceholder.typicode.com"

class APITestCase(unittest.TestCase):

    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)

    def test_get_single_post(self):
        response = requests.get(f"{BASE_URL}/posts/1")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("title", data)
        self.assertIsInstance(data["id"], int)

    def test_invalid_post(self):
        response = requests.get(f"{BASE_URL}/posts/9999")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
