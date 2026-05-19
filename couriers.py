import csv
from display import display_header

#---------------CSV FUNCTIONS---------------------


# FUNCTION TO EXTRACT COURIER DATA FROM CSV
def load_couriers():
    couriers_list = []
    with open('couriers.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            couriers_list.append(dict(row))
    return couriers_list


# FUNCTION TO SAVE COURIER DATA TO CSV NEEDED
def save_couriers_to_csv(couriers):
    with open("couriers.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "phone"])

        for courier in couriers:
            writer.writerow([courier["name"], courier["phone"]])

#---------------APP FUNCTIONS---------------------
# Couriers Menu:
def display_courier_menu():
    display_header("Couriers")
    print("\n0: Return to main menu")
    print("1: View couriers")
    print("2: Add a courier")
    print("3: Update courier information")
    print("4: Delete courier information")

def view_couriers(couriers):
    print("\nCouriers List:")
    for index, courier in enumerate(couriers):
        print(f"{index}: {courier['name']} - {courier['phone']}")

def add_courier(couriers):
    new_courier = input("\nEnter courier name: ")
    new_courier_phone = input("Enter courier phone number: ")
    couriers.append({'name': new_courier, 'phone': new_courier_phone})
    print(f"\n{new_courier} - {new_courier_phone} added to the courier list.")


def update_courier(couriers):
    print("\nHere are the current couriers:")

    for index, courier in enumerate(couriers):
        print(f"{index}: {courier['name']} - {courier['phone']}")

    courier_to_update = input("\nSelect the courier you would like to change: ")

    if courier_to_update.isdigit():
        courier_to_update_index = int(courier_to_update)

        if courier_to_update_index >= 0 and courier_to_update_index < len(couriers):
            new_courier_name = input("Enter new courier name: ")
            new_courier_phone = input("Enter new courier's phone number: ")
            couriers[courier_to_update_index]['name'] = new_courier_name
            couriers[courier_to_update_index]['phone'] = new_courier_phone
            print(f"\nCourier successfully updated! {new_courier_name} - {new_courier_phone}")
        else:
            print("Invalid index entered.")
    else:
        print("Please enter a number.")


def delete_courier(couriers):
    print('Here are the current couriers:')
    # Print courier names and indexes.
    for i in range(len(couriers)):
        print(f'{i}: {couriers[i]["name"]} - {couriers[i]["phone"]}')

    # Moved outside the loop so it only asks once
    courier_to_del = int(input("Enter the index of the courier to remove: "))

    target = couriers.pop(courier_to_del)
    print(f"{target['name']} has been deleted from the courier list.")

