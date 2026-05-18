import psycopg2
import os
import csv
from dotenv import load_dotenv
from instructions import *

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

try:

    ### SETUP THE DATABASE CONNECTION
    print('Opening connection...')
    conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'
    # Establish a database connection
    with psycopg2.connect(conn_string) as connection:

        print('Opening cursor...')
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS products;")

        print('Creating table...')
        create_table_sql = create_table()
        cursor.execute(create_table_sql)
    
# ============================================
#                 LOAD

        print("Loading products from CSV...")

        with open("Team-Pythons-Mini-Project/products.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                cursor.execute(
                    "INSERT INTO products (product_name, price) VALUES (%s, %s);",
                    (row["name"], row["price"])
                )

        print('Commiting. . .')
        connection.commit()

        print('Displaying all records. . .')
        cursor.execute("SELECT * FROM products;")
        records = cursor.fetchall()
        for row in records:
            print(row)

        print('Closing cursor. . .')
        cursor.close()

        # The connection will automatically close here
except Exception as ex:
    print('Failed to:', ex)

# Leave this line here!
print('All done!')
