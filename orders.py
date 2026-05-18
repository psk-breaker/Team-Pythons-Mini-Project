import csv
from display import display_header

#---------------CSV STUFF---------------------


def create_order_menu():
    orders_list = []
    try:
        with open('orders.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                orders_list.append(dict(row))
        return orders_list
    except FileNotFoundError:
        return []



#---------------APP FUNCTIONS---------------------
# Orders Menu:
def display_order_menu():
    display_header("Orders")
    print("\n0: Return to main menu")
    print("1: View orders")
    print("2: Add order")
    print("3: Update order status")
    print("4: Update order info")
    print("5: Delete order")

def view_orders(orders):
    print("\nOrders List:")
    for index, order in enumerate(orders):
        print(f"{index}: {order}")



def add_order(orders):
    customer_name = input('Enter the customer name:  ')
    customer_address = input('Enter the customer address:  ')
    customer_phone_number = input('Enter the customer phone number:  ')

    order = {}
    order['customer_name'] = customer_name
    order['customer_address'] = customer_address
    order['customer_phone_number'] = customer_phone_number
    order['status'] = 'preparing'

    orders.append(order)

def update_order_status(orders):
    print("--- Current Orders ---")
    for index, item in enumerate(orders):
        print(f"Index [{index}]: {item['customer_name']} - {item['status']}")

    # EVERYTHING BELOW MUST BE PUSHED INWARD
    order_to_update = input("Enter the index of the order to update status: ")

    if order_to_update.isdigit():
        order_to_update_index = int(order_to_update)

        if 0 <= order_to_update_index < len(orders):
            print("0: preparing")
            print("1: out-for-delivery")
            print("2: delivered")

            status_choice = input("Choose new status: ")

            if status_choice == "0":
                orders[order_to_update_index]['status'] = "preparing"
            elif status_choice == "1":
                orders[order_to_update_index]['status'] = "out-for-delivery"
            elif status_choice == "2":
                orders[order_to_update_index]['status'] = "delivered"
            else:
                print("Invalid choice")

            print("Order status updated!")
        else:
            print("Index out of range")
    else:
        print("Please enter a number")



def update_order_details(orders):
    print("--- Current Orders ---")
    for index, item in enumerate(orders):
        print(f"Index [{index}]: {item['customer_name']} - {item['status']}")

    order_to_update = input("Enter the index of the order to update: ")

    if order_to_update.isdigit():
        order_to_update_index = int(order_to_update)

        if order_to_update_index >= 0 and order_to_update_index < len(orders):
            selected_order = orders[order_to_update_index]

            print("Updating orders. Press Enter to keep the current value.")

            new_order_name = input("New Name (" + selected_order['customer_name'] + "): ")
            if new_order_name != "":
                selected_order['customer_name'] = new_order_name

            new_phone = input("New Phone Number (" + selected_order['customer_phone_number'] + "): ")
            if new_phone != "":
                selected_order['customer_phone_number'] = new_phone
            
            new_address = input("New Address (" + selected_order['customer_address'] + "): ")
            if new_address != "":
                selected_order['customer_address'] = new_address

            new_status = input("New Status (" + selected_order['status'] + "): ")
            if new_status != "":
                selected_order['status'] = new_status
            print("Update complete!")
        else:
            print("Error: Index out of range.")
    else:
        print("Error: Please enter a number.")



def delete_order(orders):
    print("Current Orders")
    for index, item in enumerate(orders): #enumerate gives a cleaner output compared to for in range
        print(f"Index [{index}], {item['customer_name']}")

    order_delete = input("Enter the index of the order you want to delete: ")

    if order_delete.isdigit(): #checks to see if its even an integer
        if int(order_delete) >= 0 and int(order_delete) < len(orders):
            orders.pop(int(order_delete))
            print(f"{orders}")
            print("Order successfully removed")
        else:
            print("Invalid index entered. Please try again")
    else:
        print("Please enter a number") # make sure to push (ask for verification first)
