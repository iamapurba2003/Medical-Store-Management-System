from database import db

# Talking to Database
cur = db.cursor()

# Records of User Registered
Queries = [
    ("CREATE TABLE IF NOT EXISTS accounts(user_name VARCHAR(60), user_password VARCHAR(50), name VARCHAR(30))"),
    ("INSERT INTO accounts(user_name, user_password, name) VALUES (%s, %s, %s)")
]


# Execution of Queries
for query in Queries:
    cur.execute(Queries[0])



# Registers a User
def register_user(user_name: str = '', user_password: str = '', name: str = '') -> tuple:
    if len(user_name) and len(user_password) and len(name) > 0:
        cur.execute(Queries[1], (user_name, user_password, name))
        db.commit()
        cur.execute("SELECT * FROM accounts")
        for x in cur:
            if x[0] == user_name:
                return x
    else:
        return "Please Enter the Correct Details"


def get_user(user_name: str = '', user_password: str = '') -> tuple:
    if len(user_name) > 0:
        cur.execute(f"SELECT * FROM accounts WHERE user_name LIKE '{user_name}' AND user_password LIKE '{user_password}'") 
        rows = cur.fetchall()
        if not rows:
            return "No user Found. Check if there is a Mistake OR Register User."
        else:
            return rows[0]

    else:
        return "Please Give Correct Username & Password, OR Login."


def main():
    # register_user('iamapurba2003', '1234', 'Apurba Ghosh')
    # register_user('himangshuishere', 'password#$34', 'Himangshu De')
    # register_user('thearunodaya', 'arunodaya@123#$34', 'Arunodaya Biswas')
    pass


# Driver Code
if __name__ == "__main__":
    main()
