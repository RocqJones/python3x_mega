# The program will allow a user to create username n password & store in a list then verify the password.

# create user
user_name = input("Enter User Name: ")
user_password = input("Enter new password:")

user_db = []
user_db.append(user_name)
user_db.append(user_password)
# test db
# print(user_db)

# Break
for symbol in "***************************************************************************":
    print(symbol*2)

# Verify password by checking from database
print("Verify password to proceed please!!!")
verify_password=''
while verify_password != user_db[1]:
    verify_password = input("Verify password: ")
    if verify_password == user_db[1]:
        print("SUCCESS!!\n Your bank a/c 122 556 661 649")
    else:
        print("Sorry, Try again! If you forgot password type 'hint'")
        # give hint
        if verify_password == "hint":
            h = user_db[1]
            print(h[:3] + "..." + h[-3:])
