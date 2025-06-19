from app import auth

USERS = {
    "nat.lima" : "1234",
    "guest" : "tech@fase1"
}

@auth.verify_password
def verify_password(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None
