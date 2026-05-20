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
            new_product(cursor, 'Mocha', 3.50)
            new_product(cursor, 'Latte', 3.00)
            new_product(cursor, 'Espresso', 2.50)


            # fill_couriers_table()
            new_courier(cursor, "Zohran", "07418 72148")
            new_courier(cursor, "Yasmin", "07369 36939")
            new_courier(cursor, "Xavier", "07239 82391")

            # fill_orders_table()
            new_order(cursor, "Alice", "123 Main St", "07123 45678", "Preparing")
            new_order(cursor, "Bob", "456 Elm St", "07234 56789", "Out for Delivery")
            new_order(cursor, "Charlie", "789 Oak St", "07345 67890", "Delivered")


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
            print('Displaying all couriers. . .')
            cursor.execute("SELECT * FROM couriers;")
            records = cursor.fetchall()
            for row in records:
                print(row)

            couriers = []
            for courier in records:
                couriers.append({'name': courier[1], 'phone': courier[2]})


            # EXTRACT DATA FROM ORDERS TABLE
            print('Displaying all orders. . .')
            cursor.execute("SELECT * FROM orders;")
            records = cursor.fetchall()
            for row in records: 
                print(row)

            orders = []
            for order in records:
                orders.append({
                    'customer_name': order[1],
                    'customer_address': order[2],
                    'customer_phone_number': order[3],
                    'status': order[4]
                })


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
        print('Opening connection...')
        conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'
        with psycopg2.connect(conn_string) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()

            print('Loading products into database...')
            inserted = 0
            for product in Products:
                if 'name' in product and 'price' in product:
                    name = product['name']
                    price = product['price']
                elif 'product_name' in product and 'price' in product:
                    name = product['product_name']
                    price = product['price']
                else:
                    print('Skipping invalid product entry:', product)
                    continue
                cursor.execute(
                    "INSERT INTO products (product_name, price) VALUES (%s, %s);",
                    (name, float(price))
                )
            inserted += 1
            connection.commit()
            print(f'Inserted {inserted} product records.')






              #LOAD ORDERS INTO DATABASE
            print('Loading orders into database...')
            for order in orders: 
                cursor.execute(
                    """
                    INSERT INTO orders (
                    customer_name,
                    customer_address,
                    customer_phone_number,
                    status
                    )
                    VALUES (%s, %s, %s, %s);
                    """,
                    (
                        order["customer_name"],
                        order["customer_address"],
                        order["customer_phone_number"],
                        order["status"]
                    ))
                connection.commit()
                print("Orders loaded into database successfully")

            

            print('\nClosing cursor. . .')
            cursor.close()
            print('All done!')


    except Exception as ex:
        print('Failed to:', ex)

    print('Connection closed.')


# =================================================================================
# =================================================================================

# test area for running the connection functions

create_database_tables()
extract_from_database()


