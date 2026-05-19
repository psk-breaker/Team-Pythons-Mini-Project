
def create_product_table():
    result = """
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                product_name VARCHAR(20) NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            );
            """
    return result


def create_courier_table():
    result = """
            CREATE TABLE IF NOT EXISTS couriers (
                id SERIAL PRIMARY KEY,
                courier_name VARCHAR(20) NOT NULL,
                phone_number VARCHAR(11) NOT NULL
            );
            """
    return result

def create_order_table():
    result = """
    CREATE TABLE IF NOT EXISTS Orders (
        id SERIAL PRIMARY KEY,
        customer_name VARCHAR(100) NOT NULL,
        customer_address VARCHAR(255) NOT NULL,
        customer_phone_number VARCHAR(20) NOT NULL,
        status VARCHAR(50) NOT NULL DEFAULT 'Pending'
    );
    """  

# ============================================

def insert_into_products_table():
    result = """
            INSERT INTO products (product_name, price) 
            VALUES (%s, %s) 
            RETURNING id;
            """
    return result


def new_product(cursor, v1, v2): 
    print('Inserting new product...')
    insert = insert_into_products_table()
    values = (f'{v1}', f'{v2}')
    cursor.execute(insert, values)
    new_id = cursor.fetchone()[0]
    print(f'Inserted record ID: {new_id}')

def insert_into_couriers_table():
    result = """
        INSERT INTO couriers (courier_name)
        VALUES (%s)
        RETURNING courier_id;
        """
    return result 
    
# ============================================


# def insert_into_couriers_table():

# def new_courier(cursor, v1, etc):


# ============================================


# def insert_into_orders_table():

# def new_order(cursor, v1, etc):



# ============================================
#                FILL TABLES FROM CSV


# def fill_products_table():

# def fill_couriers_table():

# def fill_orders_table():


# ============================================
#      FILL CSV FILES FROM DATABASE TABLES


# def fill_csv_from_products_table():

# def fill_csv_from_couriers_table():

# def fill_csv_from_orders_table():

