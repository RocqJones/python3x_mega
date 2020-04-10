import sqlite3

def create_db_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
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

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()

# Check options
print("Pick Options; To INSERT: '1', VIEW: '2', DELETE: '3', UPDATE:'4'")
option = input("Enter option: ")
if option == "1":
    input_item = input("Enter Item Name: ")
    input_qnty = int(input("Enter Quantity: "))
    input_price = input("Enter Price: ")
    insert(input_item, input_qnty, input_price)

elif option == "2":
    print(view())

elif option == "3":
    print(view())
    del_item = input("Enter item name to DELETE: ")
    delete(del_item)
    print(view())

elif option == "4":
    print(view())
    # update
    update_quantity = int(input("Quantity Update: "))
    update_price = input("Price Update: ")
    which_item = input("Which item ? ")
    update(update_quantity,update_price,which_item)
    print(view())

else:
    print("Invalid input")