import requests
from unittest.mock import patch
import unittest

def fusionauth_login(login_id, password, application_id, base_url="https://sandbox.fusionauth.io"):
    url = f"{base_url}/api/login"
    headers = {"Content-Type": "application/json"}
    data = {
        "loginId": login_id,
        "password": password,
        "applicationId": application_id
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return {"status": "success", "token": response.json().get("token")}
    elif response.status_code == 404:
        return {"status": "error", "message": "User not found or incorrect password"}
    elif response.status_code == 423:
        return {"status": "error", "message": "User account is locked"}
    else:
        return {"status": "error", "message": "Unknown error"}

class TestFusionAuthLogin(unittest.TestCase):
    
    @patch("requests.post")
    def test_successful_login(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "token": "fake-jwt-token",
            "user": {"id": "12345", "email": "test@example.com"}
        }

        result = fusionauth_login("test@example.com", "correct-password", "app-123")
        self.assertEqual(result["status"], "success")
        self.assertIn("token", result)
    
    @patch("requests.post")
    def test_invalid_credentials(self, mock_post):
        mock_post.return_value.status_code = 404
        mock_post.return_value.json.return_value = {}

        result = fusionauth_login("test@example.com", "wrong-password", "app-123")
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["message"], "User not found or incorrect password")

    @patch("requests.post")
    def test_unknown_error(self, mock_post):
        mock_post.return_value.status_code = 500
        mock_post.return_value.json.return_value = {}

        result = fusionauth_login("test@example.com", "password", "app-123")
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["message"], "Unknown error")

if __name__ == "__main__":
    unittest.main()