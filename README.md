# api-test-suite
 Python-based test suite for validating a public API using unittest.
# API Test Suite

This is a simple Python test suite using `unittest` to validate the functionality of a public REST API.

## 🔧 What It Tests
- Valid GET request to `/users`
- Single resource check for `/posts/1`
- 404 error check for invalid post

## 🧪 Tech Used
- Python 3
- requests
- unittest

## 🚀 How to Run
```bash
pip install requests
python test_api.py
