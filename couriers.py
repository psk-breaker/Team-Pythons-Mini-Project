import csv
from display import display_header

#---------------CSV FUNCTIONS---------------------


# FUNCTION TO EXTRACT COURIER DATA FROM CSV
def load_couriers():
    couriers_list = []
    with open('Team-Pythons-Mini-Project/couriers.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            couriers_list.append(dict(row))
    return couriers_list


# FUNCTION TO SAVE COURIER DATA TO CSV NEEDED


#---------------APP FUNCTIONS---------------------
# Couriers Menu:
def display_courier_menu():
    display_header("Couriers")
    print("\n0: Return to main menu")
    print("1: View couriers")
    print("2: Add a courier")
    print("3: Update courier information")
    print("4: Delete courier information")

# FUNCTION TO ADD A COURIER NEEDED
def add_courier(couriers):
    new_courier = input("\nEnter courier name: ")
    couriers.append(new_courier)
    print(f"\n{new_courier} added to the courier list.")


def update_courier(couriers):
    print("\nHere are the current couriers:")

    for index, courier in enumerate(couriers):
        print(f"{index}: {courier}")

    courier_to_update = input("\nSelect the courier you would like to change: ")

    if courier_to_update.isdigit():
        courier_to_update_index = int(courier_to_update)

        if courier_to_update_index >= 0 and courier_to_update_index < len(couriers):
            new_courier_name = input("Enter new courier name: ")
            new_courier_vehicle = input('Enter new couriers vehicle: ')
            couriers[courier_to_update_index]['name'] = new_courier_name
            couriers[courier_to_update]['vehicle'] = new_courier_vehicle
            print("\nCourier successfully updated!")
        else:
            print("Invalid index entered.")
    else:
        print("Please enter a number.")


def delete_courier(couriers):
    print('Here are the current couriers:')
    # Print courier names and indexes.
    for i in range(len(couriers)):
        print(f'{i} {couriers[i]}') 

    # Moved outside the loop so it only asks once
    courier_to_del = int(input("Enter the index of the courier to remove: "))

    couriers.pop(courier_to_del)
    print(couriers)
    print("Courier successfully removed")

