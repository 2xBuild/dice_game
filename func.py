import data_parser as dt

def checkUser(users,user):
    for u in users:
        if u['username'] == user.lower():
            return True
    return False

def checkPassw(users, username, password):
    for u in users:
        if u['username'] == username.lower():
            return u['password'] == password
    return False

def checkBalance(users,user):
    for u in users:
        if u['username'] == user.lower():
            return u['balance']
    return False

def updateBalance(users,username,balance):
    for u in users:
        if u['username'] == username.lower():
            u['balance'] = balance
            dt.save_users()
            return True
    return False


    
