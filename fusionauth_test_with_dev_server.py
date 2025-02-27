import requests

BASE_URL = "http://localhost:9011"
APPLICATION_ID = "e9fdb985-9173-4e01-9d73-ac2d60d1dc8e"  
API_KEY = "33052c8a-c283-4e96-9d2a-eb1215c69f8f-not-for-prod" 

def fusionauth_login(login_id, password, application_id):
    """
    Function to authenticate a user against FusionAuth.
    """
    url = f"{BASE_URL}/api/login"
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }
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
    else:
        return {"status": "error", "message": f"Unknown error: {response.text}"}


def test_successful_login():
    """
    Test successful authentication with correct credentials.
    The user must exist in FusionAuth before running this test.
    """
    result = fusionauth_login("richard@example.com", "password", APPLICATION_ID)
    assert result["status"] == "success"
    assert "token" in result


def test_invalid_credentials():
    """
    Test authentication with invalid credentials.
    """
    result = fusionauth_login("richard@example.com", "wrong-password", APPLICATION_ID)
    assert result["status"] == "error"
    assert result["message"] == "User not found or incorrect password"


def test_unknown_error():
    """
    Test handling of unknown errors by using an invalid application ID.
    """
    result = fusionauth_login("richard@example.com", "password", "INVALID_APP_ID")
    assert result["status"] == "error"
    assert "Unknown error" in result["message"]