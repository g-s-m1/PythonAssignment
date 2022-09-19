import re

def choice():
    ch = int(input("Please select what would you like to do\n1.Register\n2.Login\n3.Forgot Password\n"))
    if ch == 1:
       return register()
    elif ch == 2:
       return login()
    elif ch==3:
        return forgotpass()
    else:
       print("Incorrect choice\n")
       choice()
       
def register():
    n=0
    username = str(input("Enter Username: "))
    password = str(input("Enter Password: "))
    unpattern = "[A-Za-z0-9]+[A-Za-z0-9]*@[A-Za-z]+.[A-Z|a-z]{2,}"
    pwpattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,15}$"
    un = re.compile(unpattern)                
    unpat = re.search(un, username)
    pw = re.compile(pwpattern)                
    pwpat = re.search(pw, password)
    f = open("LoginCred.txt",'r')
    data = f.read()
    if username in data:
        print("\nUserame already taken. Please use a different username.\n")
        return register()
    if unpat:
        n=n+1
    else:
        print("\nUsername format is invalid\n")
        return register()
    if pwpat:
        n=n+1
    else:
        print("\nPassword format is invalid\n")
        return register()
    f.close()
    f = open("LoginCred.txt",'a')
    f.write("\n")
    f.write(username + " " + password)
    if(n==2):
        print("\nRegistration Successful\n")
        return
    
    
    
def login():
    username = str(input("Enter Username: "))
    password = str(input("Enter Password: "))
    f = open("LoginCred.txt",'r')
    data = f.read()
    data = data.split()
    if username in data:
        index = data.index(username) + 1
        pw = data[index]
        if pw == password:
            print("\nLogin Successful!!!!!")
            return
        else:
            print("Password entered is wrong\n")
            return choice()
    else:
        print("Username not found. Please Register")

def forgotpass():
    username = str(input("Enter Username: "))
    y=int(input("\n1.Would you like to retrieve your password?\n2.Change password\n"))
    f = open("LoginCred.txt",'r')
    data = f.read()
    data = data.split()
    if username in data:
        index = data.index(username) + 1
        if(y==1):
            pw = data[index]
            print("\nYour password is "+ pw)
            return
        elif(y==2):
            password=str(input("Enter Password: "))
            pw = data[index]
            pwpattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,15}$"
            pw1 = re.compile(pwpattern)                
            pwpat = re.search(pw1, password)
            data1=f.read()
            if pwpat:
                data1=data1.replace(pw,password)
                f = open("LoginCred.txt",'a')
                f.write(data1)
                print("\nPassword changed successfully\n")
                return
            else:
                print("\nPassword format is invalid\n")
                return forgotpass()
    else:
        print("Username not found.")
        return choice()

    
choice()
