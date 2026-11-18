def test_login(user, password):
    if user == "admin" and password == "1234":
        print("successful")
    else:
        print("failed")


test_login("admin", "1234")
test_login("user", "0000")
