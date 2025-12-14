def login_user(username, password):
    if username:
        if password:
            if len(username) > 3:
                if len(password) > 5:
                    if username == "testuser":
                        if password == "password123":
                            return {"message": "Login successful"}
                        else:
                            return {"message": "Invalid password"}
                    else:
                        if username == "admin":
                            if password == "adminpass":
                                return {"message": "Admin login successful"}
                            else:
                                return {"message": "Invalid admin password"}
                        else:
                            return {"message": "User not found"}
                else:
                    return {"message": "Password too short"}
            else:
                return {"message": "Username too short"}
        else:
            return {"message": "Password is required"}
    else:
        return {"message": "Username is required"}