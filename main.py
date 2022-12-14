def register():
    db = open("database.txt", "r")
    Username = input("Create Username: ")
    Password = input("Create Password: ")
    data = {}

    for user in db:
        username, password = user.split(",")
        password = password.strip()
        data[username] = password

    import re
    username_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    password_regex = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,16}$")

    if not re.fullmatch(username_regex, Username):
        print("Invalid Email")
        register()
    elif not re.fullmatch(password_regex, Password):
        print("Password too weak")
        register()
    elif Username in data:
        print("Username already exist")
        register()
    else:
        db = open("database.txt", "a")
        db.write(Username + ", " + Password + "\n")
        print("Registration done successfully!")

def access():
    db = open("database.txt", "r")
    Username = input("Enter your Username: ")
    Password = input("Enter your Password: ")

    if not len(Username or Password) < 1:
        data = {}
        for user in db:
                username, password = user.split(",")
                password = password.strip()
                data[username] = password
        try:
            if data[Username]:
                if Password == data[Username]:
                    print("Login Successful")
                    print("Hi,", Username)
                else:
                    print("Incorrect Username or Password")
            else:
                print("Username doesn't exist")
        except:
            print("Login Error")

def home(option = None):
    option = input("Choose Login | Signup: ")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option")
        home()

home()

