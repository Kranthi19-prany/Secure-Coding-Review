import hashlib
import json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register the user 'kranthi akula'
def register_user():
    users = {
        "kranthi akula": hash_password("kranthi@123")
    }

    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    print("User 'kranthi akula' registered successfully.")

register_user()
import hashlib
import hmac
import json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(username, password):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)

        if username in users:
            stored_hash = users[username]
            input_hash = hash_password(password)

            if hmac.compare_digest(stored_hash, input_hash):
                print("Login successful!")
                return True
            else:
                print("Invalid password.")
        else:
            print("Username not found.")
    except Exception as e:
        print("Error:", e)

    return False

# 🔐 Prompt login
username_input = input("Enter username: ")
password_input = input("Enter password: ")
login(username_input, password_input)
