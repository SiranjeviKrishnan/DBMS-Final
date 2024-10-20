import mysql.connector

# Establish a connection
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Olympics_21274501"
)

# Create a cursor object
cursor = cnx.cursor()

# Execute a query
cursor.execute("SELECT * FROM Events")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()