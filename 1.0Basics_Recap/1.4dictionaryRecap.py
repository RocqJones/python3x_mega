# Has a Keys and Value
d = {"Name":"Kain", "Age":22, "Location":"Kenya"}

print(d)

# Parse the Keys to access the value
print(d["Name"])
print(d["Age"])
print(d["Location"])

# Longer values example; city
df = {"Name":"Will Luivy", "Age":44, "City":("Kenya", "New Jersey", "Germany", "California")}
print(df["Name"])
print(df["City"])
print(df["City"][1])