
def create_table():
    result = """
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                product_name VARCHAR(20) NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            );
            """
    return result

def create_couriers_table():
    result = """
            CREATE TABLE couriers(
            courier_id SERIAL PRIMARY KEY,
            courier_name VARCHAR(100)
            );
            """
    return result 