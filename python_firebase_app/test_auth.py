import requests

BASE_URL = "http://127.0.0.1:5000"
test_email = "testuser_auto_123@example.com"
test_password = "password123"

# Create a session to persist cookies
session = requests.Session()

def test_home():
    print("Testing Home page...")
    r = session.get(BASE_URL + "/")
    assert r.status_code == 200, f"Home page returned {r.status_code}"
    assert b"Car Rental Portal" in r.content, "Home page missing title"
    print("Home page OK.")

def test_register():
    print("Testing Registration...")
    data = {
        "fullname": "Test User",
        "emailid": test_email,
        "password": test_password
    }
    r = session.post(BASE_URL + "/register", data=data, allow_redirects=False)
    # Registration should redirect to /
    if r.status_code == 302:
        print("Registration redirected to Home (Success)")
    elif r.status_code == 400:
        if b"EMAIL_EXISTS" in r.content:
            print("User already exists, proceeding to test login.")
        else:
            print("Registration failed:", r.content)
    else:
        print(f"Unexpected status code: {r.status_code}")

def test_login():
    print("Testing Login...")
    data = {
        "email": test_email,
        "password": test_password
    }
    r = session.post(BASE_URL + "/login", data=data, allow_redirects=False)
    if r.status_code == 302:
        print("Login redirected to Home (Success)")
        
        # Verify if session is established by hitting home page and checking for "Logout"
        r2 = session.get(BASE_URL + "/")
        if b"Logout" in r2.content:
            print("User successfully authenticated, Logout button found.")
        else:
            print("WARNING: Logout button not found on home page after login.")
    else:
        print(f"Login failed: {r.status_code} {r.content}")

def test_logout():
    print("Testing Logout...")
    r = session.get(BASE_URL + "/logout", allow_redirects=False)
    if r.status_code == 302:
        print("Logout redirected to Home (Success)")
        r2 = session.get(BASE_URL + "/")
        if b"Login / Register" in r2.content:
            print("User successfully logged out, Login button found.")
        else:
            print("WARNING: Login button not found after logout.")
    else:
        print(f"Logout failed: {r.status_code}")

if __name__ == "__main__":
    test_home()
    test_register()
    test_login()
    test_logout()
