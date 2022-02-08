# Module specific import(s)
import getpass

# App specific import(s)
from database import db
from loginStatus import get_user_logged_status
from login_logoutMod import login, logout, register
from medicineStock import Medicines
from userAccount import register_user, get_user
from menu import menu

# Making a Cursor to talk to Database
cur = db.cursor()

# Queries





def main(userInput:int=0):
    menu()
    userInput = input("Enter Your Choice? ")
    print()
    while userInput != 'q':
    

        if userInput == '1':
            print('Medicine Name and Price:')
            print()
            for items in Medicines:
                print(items[0],' ----> ','Rs.', items[1])
            menu()

        if userInput == '2':
            uName = input("Enter username: ")
            if get_user_logged_status(uName) == 'true':
                print('Medicines Ordered: ')
                menu()
            
            else:
                if get_user_logged_status(uName) == 'false':
                    print('Please Log In to Continue!')
                    menu()
        
        if userInput == '3':
            uName = input('Enter username: ')
            uPass = getpass.getpass('Enter password: ')
            a = login(uName, uPass)
            if a == 'true':
                print(a)
                menu()
            else:
                print(a)
                menu()
        
        if userInput == '4':
            uName = input('Enter username: ')
            a = logout(uName)
            if a == 'true':
                print(a)
                menu()
            else: print(a);menu()

        if userInput == '5':
            uName = input('Enter username: ')
            uPass = getpass.getpass('Enter password: ')
            a = get_user(uName, uPass)
            if type(a) == tuple:
                print()
                print(f'Your Name: {a[2]}\nYour username:{a[0]}')
                print()
                menu()
            else: print(a);menu()

        if userInput == '6':
            uFullName = input('Enter your full name: ')
            uName1 = input('Enter a username: ')
            uPass1 = getpass.getpass('Enter a password: ')
            register(uName1)
            a = register_user(uName1, uPass1, uFullName)
            if type(a) == tuple: print(f'You have been registered successfully!');menu()
            else: 
                print(a)
                menu()
        if userInput not in '123456':
            print("Sorry Your Option Does not Match any of the given Choices.")
            menu()
        print()
        userInput = input("Enter Your Choice? ")
        print()

# Driver Code
if __name__ == "__main__":
    main()
