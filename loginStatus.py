from database import db

# Talking to Database
cur = db.cursor()

# Drafting Queries
Queries = [
    ("CREATE TABLE IF NOT EXISTS userStatus( user_name VARCHAR(60), status VARCHAR(40))")
]

# Executing Queries
for query in Queries:
    cur.execute(Queries[0])

# cur.execute("SHOW TABLES")
# for x in cur:
#     print(x)


def get_user_logged_status(user_name: str = '') -> bool:
    if len(user_name) > 0:
        cur.execute(f"SELECT status FROM userStatus WHERE user_name='{user_name}'")
        rows = cur.fetchall()
        if not rows:
            return f"No User Found with the Username {user_name}. Please Register"
        else:
            return rows[0][0]
        
    else:
        return "Please Check if your entered Username is Correct or not. Else Register ... "
    








def main():
    pass


# Driver Code
if __name__ == "__main__":
    main()
