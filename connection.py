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

            cursor.execute("DROP TABLE IF EXISTS orders;")
            print('Creating Order table...')
            create_order_table_sql = create_order_table()
            cursor.execute(create_order_table_sql)
            print('Order table created successfully.')



    # ============================================
    #                FILL TABLES FROM CSV

            print('Filling tables from CSV files...')

            # EXAMPLE
            new_product(cursor, 'Pizza', 9.99)


            # fill_products_table()
            # aalamm done

            # fill_couriers_table()
            new_courier(cursor, "Zohran", "07418 72148")
            new_courier(cursor, "Yasmin", "07369 36939")
            new_courier(cursor, "Xavier", "07239 82391")

            # fill_orders_table()
            # ishak


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

            # EXTRACT DATA FROM PRODUCT TABLE
            print('Displaying all records. . .')
            cursor.execute("SELECT * FROM products;")
            records = cursor.fetchall()
            for row in records:
                print(row)

            Products = []
            for product in records:
                Products.append({'name': product[1], 'price': product[2]})
            
            # EXTRACT DATA FROM COURIER TABLE

            couriers = 0

            # EXTRACT DATA FROM ORDERS TABLE

            orders = 0

    # ============================================
    #                 CLOSE CONNECTION

            print('\nClosing cursor. . .')
            cursor.close()
            print('All done!')

            return Products, couriers, orders
    except Exception as ex:
        print('Failed to:', ex)

    print("Connection closed.")


# ==================================================================================
# ==================================================================================


def load_into_database(Products, couriers, orders):
    try:
        conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'
        # Establish a database connection
        with psycopg2.connect(conn_string) as connection:

            print('Opening cursor...')
            cursor = connection.cursor()

        print('Loading couriers into database...')

        for courier in couriers:
            cursor.execute(
        "INSERT INTO couriers (name, phone) VALUES (%s, %s)",
        (
            courier["name"],
            courier["phone_number"]
        )
        )

        connection.commit()
        print("Couriers loaded into database successfully")
        
    except Exception as ex:
        print('Failed to:', ex)
        # pull lists of products, couriers, orders from app.py into here
        # and push them into database
    

    # ============================================
    #                 CLOSE CONNECTION

        print('\nClosing cursor. . .')
            # cursor.close()
        print('All done!')

            # The connection will automatically close here
    except Exception as ex:
        print('Failed to:', ex)

    print("Connection closed.")


# =================================================================================
# =================================================================================

# test area for running the connection functions

create_database_tables()
extract_from_database()
