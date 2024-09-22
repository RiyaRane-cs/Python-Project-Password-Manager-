

    
        
#             Add()
# print(new_username)
        

def View():
    with open('passwords.txt','r') as f:
        for lines in f.readlines():
            print(lines.rstrip())
def Add():
    global new_pswd
    new_username=input("Enter new username:")
    new_pswd=input("Enter new password:")
    with open('passwords.txt','a') as f:
        f.write(new_username+"|"+new_pswd+"\n") 

def Change():
    with open('passwords.txt','r') as f:
        
        for rlines in f.read():
            print(rlines.rstrip(),end="")
        print()
    chng_pswrd=input("Enter the old password that u want to change:")
        
    new_pswd1=input("Enter the new password:")
    with open('passwords.txt', 'r') as f: 
        data = f.read() 
        data = data.replace(chng_pswrd, new_pswd1) 
    with open('passwords.txt', 'w') as f:
        f.write(data)
        
        

while True:
    mode=int(input('''Would operation u want to perform
            1. View Existing Passwords and Usernames
            2. Add New Username and password to Existing ones
            3. Change the password of a particular username:
            4. Exit'''))
    if mode==1:
        View()
        
    elif mode==2:
        Add()
        
    elif mode==3:
        Change()
    elif mode==4:
        break
    else:
        print("Invalid Mode")
        break
        