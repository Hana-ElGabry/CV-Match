import sqlite3

# Connect to the database
connection = sqlite3.connect('store.db')
cursor = connection.cursor()

# Create tables
command1 = """
CREATE TABLE IF NOT EXISTS stores(
    store_id INTEGER PRIMARY KEY,
    location TEXT
)
"""
cursor.execute(command1)

command2 = """
CREATE TABLE IF NOT EXISTS purchases(
    purchase_id INTEGER PRIMARY KEY,
    store_id INTEGER,
    total_cost FLOAT,
    FOREIGN KEY(store_id) REFERENCES stores(store_id)
)
"""
cursor.execute(command2)

# Insert data into the tables
cursor.execute("INSERT INTO stores VALUES(1, 'New York')")
cursor.execute("INSERT INTO stores VALUES(2, 'Los Angeles')")
cursor.execute("INSERT INTO stores VALUES(3, 'Chicago')")

cursor.execute("INSERT INTO purchases VALUES(1, 1, 100)")
cursor.execute("INSERT INTO purchases VALUES(2, 1, 200)")
cursor.execute("INSERT INTO purchases VALUES(3, 2, 300)")

# Commit changes to save data
connection.commit()

# Query and fetch results
cursor.execute("SELECT * FROM stores")
results = cursor.fetchall()
print(results)

# Close the connection
connection.close()
