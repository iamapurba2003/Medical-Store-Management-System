from database import db

# Talking to Database
cur = db.cursor()

# Queries
Queries = []


def login(user_name: str = '', user_password: str = '') -> bool:
    if len(user_name) and len(user_password) > 0:
        cur.execute(f"SELECT user_name FROM userStatus WHERE user_name='{user_name}'")
        rows = cur.fetchall()
        if not rows:
            return "User Does not Exists"
        else:
            cur.execute(f"SELECT status AS userStatus FROM userStatus WHERE user_name='{user_name}'")
            for x in cur:
                data = x[0]
            if data == "false":
                cur.execute(f"SELECT user_password FROM accounts WHERE user_name='{user_name}'")
                rows = cur.fetchall()
                if rows[0][0] == user_password:
                    cur.execute(f"UPDATE userStatus SET status='true' WHERE user_name='{user_name}'")
                    db.commit()
                    cur.execute(f"SELECT status AS userStatus FROM userStatus WHERE user_name='{user_name}'")
                    for x in cur:
                        if x[0] == 'true':
                            return f'User Logged in Successfully with Username {user_name}'
                        else:
                            return "Sorry the User is not logged in. Some Error Occured"
                else:
                    return "Password Incorrect"
            else:
                return "User Already Logged In"
            
            
def logout(user_name: str = ''):
    if len(user_name) > 0:
        cur.execute(f"SELECT user_name FROM userStatus WHERE user_name{user_name}'")
        rows = cur.fetchall()
        if not rows:
            return "User Does not Exists"
        else:
            cur.execute(f"SELECT status AS userStatus FROM userStatus WHERE user_name='{user_name}'")
            for x in cur:
                data = x[0]
            if data == "true":
                cur.execute(f"UPDATE userStatus SET status='true' WHERE user_name='{user_name}'")
                db.commit()
                cur.execute(f"SELECT status from userStatus WHERE user_name='{user_name}'")
                for x in cur:
                    if x[0] == 'true':
                        return f"User not Logged Out Successfully. Try Again!"
                    else:
                        return f"User Logged out Successfully."
                        
    else:
        return "Incorrect Username"
    pass


def main():
    logout('iamapurba2003')
    pass


if __name__ == "__main__":
    main()
# Query Execution
# cur.execute(Queries[0])
# db.commit()
# cur.execute("SELECT status AS UserStaus FROM userStatus")
# for x in cur:
#     print(x)
