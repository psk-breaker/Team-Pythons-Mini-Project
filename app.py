from products import *
from orders import *
from couriers import *
from display import *
from save import *
from connection import *

# ================================================================================

extract_from_database
Products = create_product_menu()
orders = create_order_menu()
couriers = load_couriers()


# ================================================================================


is_app_running = True

while is_app_running == True:
    display_main_menu()
    choice = int(input("\nSelect 0, 1, 2 or 3: "))

    if choice == 0: 
        # load_into_database()
        save_products_to_csv(Products)
        save_orders_to_csv(orders)
        save_couriers_to_csv(couriers)

        print("Exiting app") 
        is_app_running = False # This will finally fail the while loop condition


# ==================================================================================
# This is our product side of the app

    elif choice == 1: 
        display_product_navigation_menu()
        product_choice = int(input("\nChoose an Option: "))

        if product_choice == 0:
            print("Returning to Main Menu...")

        elif product_choice == 1:
            view_products(Products)

        elif product_choice == 2:
            add_product(Products)
 
        elif product_choice == 3:
            update_product(Products)

        elif product_choice == 4:
            delete_product(Products) 


# ============================================================================
# This is the order side of the app

    elif choice == 2:
        
        display_order_menu()
        choice = int(input("\nChoose an Option: "))

        if choice == 0:
            print("Returning to Main Menu...")

        elif choice == 1: 
            view_orders(orders)


        elif choice == 2:
            add_order(orders) 


        elif choice == 3:
            update_order_status(orders)


        elif choice == 4:
            update_order_details(orders)


        elif choice == 5:
            delete_order(orders)



# ============================================================================
# This is the courier side of the app


    elif choice == 3:
        
        display_courier_menu()
        choice = int(input("\nChoose an Option:  "))

        if choice == 0:
            print("Returning to Main Menu...")


        elif choice == 1:
            view_couriers(couriers)


        if choice == 2:
            add_courier(couriers)

            
        if choice == 3:
            update_courier(couriers)


        if choice == 4:
            delete_courier(couriers)




