def register():
    db = open("database.txt", "r")
    Username = input("Create Username: ")
    Password = input("Create Password: ")
    U = []
    P = []
    for x in db:
        a,b = x.split(",")
        b = b.strip()
        U.append(a)
        P.append(b)
    data = dict(zip(U, P))

    import re
    UN = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    PW = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,16}$")

    if not re.fullmatch(UN, Username):
        print("Invalid Email")
        register()
    elif not re.fullmatch(PW, Password):
        print("Password too weak")
        register()
    elif Username in U:
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
        for x in db:
                a, b = x.split(",")
                b = b.strip()
                data[a] = b
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

