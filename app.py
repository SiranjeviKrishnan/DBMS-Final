import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="Olympics_21274501"
)

cursor = db.cursor()

# Execute a query and fetch results
cursor.execute("SELECT * FROM Athletes")
results = cursor.fetchall()

for row in results:
    print(row)

db.close()

