def age_foo(myage):
    new_age = myage + 2
    return new_age

# input type
age = int(input("Enter age: "))

# conditionals
if age < 100:
    print(age_foo(age))

else:
    print("That's impossible")