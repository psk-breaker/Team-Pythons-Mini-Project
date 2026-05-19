import csv
from display import display_header


#---------------CSV STUFF---------------------


def create_product_menu():
    result = []
    with open('Team-Pythons-Mini-Project/products.csv', mode='r', newline='') as data:
        reader = csv.DictReader(data)
        for row in reader:
            result.append(row)
    return result


# NEED A save_products_to_csv() FUNCTION TOO


#---------------APP FUNCTIONS---------------------
# DISPLAY_PRODUCT_NAVIGATION_MENU:
def display_product_navigation_menu():
    display_header("Products")
    print("\n0: Return to main menu")
    print("1: View products")
    print("2: Add product")
    print("3: Update product")
    print("4: Delete product")


#FUNCTION UPDATED REPLACING ELIF 1
def view_products(Products):
    print("\nProducts List: ")
    for index, product in enumerate(Products): 
        print(f"{index}: {product["name"]} - £{product["price"]}")


#FUNCTION TO REPLACE ELIF 2
def add_product(Products): 
    add_product_name = input("Enter product name: ")
    add_product_price = input(("Enter product price: "))
    new_product = {
        "name": add_product_name, 
        "price": add_product_price
    }
    Products.append(new_product)
    view_products(Products)
    print("\nProduct successfully added!")


#FUNCTION TO REPLACE ELIF 3
def update_product(Products): 
    view_products(Products)
    select_update_list = int(input("\nSelect the product you would like to change: "))

    new_product_name = input("Enter new product name: ")
    new_product_price = float(input("Enter new product price: "))

    Products[select_update_list]['name'] = new_product_name #Go to that product, then change its name
    Products[select_update_list]['price'] = new_product_price
    view_products(Products)
    print("\nProduct successfully updated!")


#FUNCTION TO REPLACE ELIF 4
def delete_product(Products): 
    view_products(Products) 
    select_delete_product = int(input("\nSelect the product you would like to remove: "))
    Products.pop(select_delete_product)
    view_products(Products)
    print("\nProduct successfully removed")

