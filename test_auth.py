import requests
import json

BASE_URL = 'http://localhost:8000/api'

def test_authentication():
    print("\n=== Testing Django REST Framework Authentication ===\n")
    
    # Test 1: Try to access without token
    print("Test 1: Accessing without token")
    try:
        response = requests.get(f"{BASE_URL}/login/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")

    # Test 2: Login with invalid credentials
    print("Test 2: Login with invalid credentials")
    try:
        response = requests.post(
            f"{BASE_URL}/login/",
            json={"username": "wrong", "password": "wrong"}
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")

    # Test 3: Login with valid credentials
    print("Test 3: Login with valid credentials")
    try:
        response = requests.post(
            f"{BASE_URL}/login/",
            json={"username": "testuser", "password": "testpass123"}
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
        if response.status_code == 200:
            token = response.json().get('token')
            
            # Test 4: Access with valid token
            print("Test 4: Accessing with valid token")
            headers = {'Authorization': f'Token {token}'}
            response = requests.get(f"{BASE_URL}/login/", headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}\n")
            
            # Test 5: Access with invalid token
            print("Test 5: Accessing with invalid token")
            headers = {'Authorization': 'Token invalid_token_here'}
            response = requests.get(f"{BASE_URL}/login/", headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    test_authentication() 