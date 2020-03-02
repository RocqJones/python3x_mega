# login
username = input("Enter Username: ")
password = input("Enter password: ")

loginDet = []
loginDet.append(username)
loginDet.append(password)
# print(loginDet)

file = open("login.txt",'w')
file.write("Username: "+loginDet[0]+"\n"+"Password: "+loginDet[1])
file.close()

# validation by reading from txt database.