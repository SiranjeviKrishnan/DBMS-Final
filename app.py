import mysql.connector
import csv
import os

# database connect
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=input("Enter MySQL username: "),
            password=input("Enter MySQL password: "),
            database="dswork"
        )
        print("Connected to MySQL database successfully!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# csv to sql
def import_csv_to_mysql(connection, csv_file, table_name):
    cursor = connection.cursor()
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{header} VARCHAR(255)' for header in headers])})"
        cursor.execute(create_table_query)
        
        insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(['%s' for _ in headers])})"
        
        for row in csv_reader:
            cursor.execute(insert_query, row)
    
    connection.commit()
    print(f"Data imported successfully into {table_name} table!")

# main
def main():
    connection = connect_to_database()
    if connection:
        csv_directory = input("Enter the directory path containing CSV files: ")
        
        for filename in os.listdir(csv_directory):
            if filename.endswith('.csv'):
                csv_file = os.path.join(csv_directory, filename)
                table_name = os.path.splitext(filename)[0]
                import_csv_to_mysql(connection, csv_file, table_name)
        
        connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()