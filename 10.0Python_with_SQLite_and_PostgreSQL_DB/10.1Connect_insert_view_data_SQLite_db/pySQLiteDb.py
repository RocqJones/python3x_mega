import sqlite3

def create_db_table():
    # 1. create connection
    conn = sqlite3.connect("lite.db")
    # 2. Create cursor object that refers to the conn
    cur = conn.cursor()
    # 3. SQLite query
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # commit changes
    conn.commit()
    # 4. Close db connection
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # This line will be prone to sql injections
    # cur.execute("INSERT INTO store VALUES ('Wine glass, 8, KSh.1,050')")
    # solution is to...
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

# insert("Wine glass", 8, 1050)
# print(view())

# Check options
print("Pick Options; To Insert data enter '1', to View data enter '2'")
option = input("Enter option: ")
if option == "1":
    input_item = input("Enter Item Name: ")
    input_qnty = int(input("Enter Quantity: "))
    input_price = input("Enter Price: ")
    insert(input_item, input_qnty, input_price)

elif option == "2":
    print(view())

else:
    print("Invalid input")