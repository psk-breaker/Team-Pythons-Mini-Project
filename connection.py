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

def create_database_tables():
    try:

<<<<<<< HEAD
    ### SETUP THE DATABASE CONNECTION
    print('Opening connection...')
    conn_string = f'host={host_name} port=5432 dbname={database_name} user={user_name} password={user_password}'
    # Establish a database connection
    with psycopg2.connect(conn_string) as connection:

        print('Opening cursor...')
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS products;")
        cursor.execute("DROP TABLE IF EXISTS couriers;")

        print('Creating table...')
        create_table_sql = create_table()
        cursor.execute(create_table_sql)
        
        print('Creating couriers table...')
        courier_table_sql = create_couriers_table()
        cursor.execute(courier_table_sql)

        


=======
        ### SETUP THE DATABASE CONNECTION
        print('Opening connection...')
        conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'
        # Establish a database connection
        with psycopg2.connect(conn_string) as connection:

            print('Opening cursor...')
            cursor = connection.cursor()

    # ============================================
    #                CREATE TABLES

            print('Creating tables...')

            cursor.execute("DROP TABLE IF EXISTS products;")
            create_table_sql = create_product_table()
            cursor.execute(create_table_sql)
            print('Product table created successfully.')

            cursor.execute("DROP TABLE IF EXISTS couriers;")
            create_table_sql = create_courier_table()
            cursor.execute(create_table_sql)
            print('Courier table created successfully.')

            #Create Order Table
            cursor.execute("DROP TABLE IF EXISTS orders;")
            print('Creating Order table...')
            create_order_table_sql = create_order_table()
            cursor.execute(create_order_table_sql)


    # ============================================
    #                FILL TABLES FROM CSV

            print('Filling tables from CSV files...')

            # EXAMPLE
            new_product(cursor, 'Pizza', 9.99)


            # fill_products_table()

            # fill_couriers_table()

            # fill_orders_table()


    # ============================================
    #                 LOAD TO DATABASE

            print('\n\nCommiting. . .')
            connection.commit()

            print('Displaying all records. . .')
            cursor.execute("SELECT * FROM products;")
            records = cursor.fetchall()
            for row in records:
                print(row)

            print('\nClosing cursor. . .')
            cursor.close()
            print('All done!')
            # The connection will automatically close here

    except Exception as ex:
        print('Failed to:', ex)





# =================================================================================
# =================================================================================
>>>>>>> 23ffa645eb8d0e0f5ad0737df89438656f0b7309
        
def extract_from_database():
    try:

    # ============================================
    #            SETUP THE DATABASE CONNECTION
        
        print('Opening connection...')
        conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'
        # Establish a database connection
        with psycopg2.connect(conn_string) as connection:

            print('Opening cursor...')
            cursor = connection.cursor()

    # ============================================
    #                EXTRACT DATA

            print('Extracting data from database...')

            print('Displaying all records. . .')
            cursor.execute("SELECT * FROM products;")
            records = cursor.fetchall()
            for row in records:
                print(row)
            
            # EXTRACT DATA FROM COURIER TABLE

            # EXTRACT DATA FROM ORDERS TABLE

    # ============================================
    #                 CLOSE CONNECTION

            print('\nClosing cursor. . .')
            # Closes the cursor so will be unusable from this point
            cursor.close()
            print('All done!')

            # The connection will automatically close here
    except Exception as ex:
        print('Failed to:', ex)

    print("Connection closed.")


