from database import db
from userAccount import register_user, get_user
from menu import menu

# Making a Cursor to talk to Database
cur = db.cursor()

# Queries





def main():
    # data = register_user() 
    data = get_user('iamapurba2003', '1234')
    print(data)

    
    pass


# Driver Code
if __name__ == "__main__":
    main()