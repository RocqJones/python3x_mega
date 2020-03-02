# # There are error that can be accepted
# def devide(a,b):
#     return a/b

# print(devide(1,2))
# print(devide(1,0)) # This will give a "ZeroDivisionError: division by zero" and the program will crush
# print(devide(15,78))

# To remove the error on ln6 do an exception. When you specify the error you exclude other errors
def devide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You can't devide by zero"

print(devide(1,2))
print(devide(1,0)) # This will give an exception and continue
print(devide(15,78))