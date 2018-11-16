import re

def validate():
    while True:
        password = input("Enter the password to check : ")
        y = len(password)
        if y > 6 and y < 20:
            if re.search('[0-9]', password) is None:
                print("Password must contain at least a number.")
            elif re.search('[A-Z]', password) is None:
                print('Password must contain at least a upper case letter.')
            elif re.search('[a-z]', password) is None:
                print("Password must contain at least a lower case letter")
            else:
                print("Password is okay")
        else:
            print("Password must be between  6 and 20.")
        
validate()
  
