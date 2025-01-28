import json

def load_users(filename="users.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error {e}")
        return []

users = load_users()



def save_users(filename="users.json"):
    try:
        with open(filename, "w") as file:
            json.dump(users, file)
            return True
    except Exception as e:
        print(f"Error {e}")


# if this file is running directly (independently)
if __name__ == "__main__":                            
    for user in users:
        print(user)
