from database import db
from userAccount import register_user, get_user

# Making a Cursor to talk to Database
cur = db.cursor()

# Queries


# Menu to be Shown to User
def menu():
    print(""" 
    1. Available Medicines
    2. Order Medicines
    3. Login
    4. Logout
    5. My Account""")  


def main():
    # data = register_user() 
    data = get_user('iamapurba2003', '1234')
    print(data)

    
    pass


# Driver Code
if __name__ == "__main__":
    main()