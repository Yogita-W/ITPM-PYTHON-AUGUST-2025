def main_menu():
    print("\n***** Hotel Management System *****")
    print("-------Select Franchise-------")
    print("1) Royal Palace, Wakad Branch")
    print("2) Royal Palace, Deccan Branch")
    print("3) Royal Palace, Katraj Branch")
    print("4) Royal Palace, Wadgaon BK Branch")
    print("5) Royal Palace, Vimannagar Branch")
    print("6) EXIT")

def branch_menu(branch_name):
    room_charges = 0
    food_charges = 0
    while True:
        print(f"\n*** Welcome to Royal Palace, {branch_name} Branch ***")
        print("1) Room Booking")
        print("2) Restaurant")
        print("3) Checkout")
        print("4) Exit to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            room_charges += room_booking()
        elif choice == '2':
            food_charges += restaurant()
        elif choice == '3':
            checkout(room_charges, food_charges)
            break  # Exit after checkout and payment
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def room_booking():
    room_types = {
        '1': ('Standard Non-AC', 1000),
        '2': ('Standard AC', 1500),
        '3': ('3-Bed Non-AC', 2000),
        '4': ('3-Bed AC', 2500)
    }
    print("\n---- SELECT ROOM TYPE ----")
    for key, (room, price) in room_types.items():
        print(f"{key}. {room} Rs. {price} per night")
    choice = input("Enter room type option:= ")
    if choice in room_types:
        nights = int(input("Enter number of nights: "))
        total = room_types[choice][1] * nights
        print(f"Room booked. Charges: Rs. {total}")
        return total
    else:
        print("Invalid room type selected.")
        return 0

def restaurant():
    menu = {
        "Breakfast": {
            '1': ('Regular Tea', 20),
            '2': ('Poha', 25),
            '3': ('Upma', 25),
            '4': ('Cold Drink', 25),
            '5': ('Bread Butter', 30),
            '6': ('Veg Sandwich', 50),
            '7': ('Cheese Toast Sandwich', 70),
            '8': ('Tomato Soup', 110),
            '9': ('Samosa', 50),
            '11': ('Kachori', 30),
            '15': ('Masala Dosa', 60),
            '16': ('Idli Sambhar', 40)
        },
        "Main Course": {
            '17': ('Paneer Butter Masala', 160),
            '18': ('Veg Biryani', 130),
            '19': ('Dal Tadka', 100),
            '20': ('Tandoori Roti', 15),
            '21': ('Mix Veg Curry', 120)
        },
        "Beverages": {
            '4': ('Cold Drink', 25),
            '22': ('Lassi', 50),
            '23': ('Coffee', 30),
            '24': ('Buttermilk', 20)
        },
        "Sweets": {
            '10': ('Jalebi', 15),
            '25': ('Gulab Jamun', 40)
        }
    }

    total = 0
    all_items = {}
    for category in menu.values():
        all_items.update(category)

    while True:
        print("\n--- Menu ---")
        for category, items in menu.items():
            print(f"\n=== {category} ===")
            for key, (name, price) in items.items():
                print(f"{key}. {name} - Rs. {price}")
        print("0. Finish Order")

        choice = input("Enter item number: ")
        if choice == '0':
            break
        elif choice in all_items:
            qty_input = input("Enter quantity: ")
            if qty_input.isdigit():
                qty = int(qty_input)
                total += all_items[choice][1] * qty
            else:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Invalid choice.")
    
    if total > 0:
        print(f"Food ordered. Charges: Rs. {total}")
    else:
        print("No items ordered.")
    return total


def checkout(room_charges, food_charges):
    total = room_charges + food_charges
    if total > 0:
        print(f"\nTotal Bill: Rs. {total}")
        payment(total)
    else:
        print("No charges to pay.")

def payment(amount):
    print("\n--- Payment Options ---")
    print("1. Cash")
    print("2. Credit/Debit Card (5% discount)")
    print("3. UPI")
    choice = input("Select payment method: ")
    if choice == "1":
        print(f"Payment of Rs. {amount} received in cash. Thank you! Please visit again.")
        exit()
    elif choice == "2":
        discount = amount * 0.05
        discounted_amount = amount - discount
        print(f"5% discount applied. You saved Rs. {discount:.2f}")
        print(f"Payment of Rs. {discounted_amount:.2f} received via Credit/Debit Card. Thank you! Please visit again.")
        exit()
    elif choice == "3":
        print(f"Payment of Rs. {amount} received via UPI. Thank you! Please visit again.")
        exit()
    else:
        print("Invalid payment method.")



def main():
    branches = {
        '1': 'Wakad',
        '2': 'Deccan',
        '3': 'Katraj',
        '4': 'Wadgaon BK',
        '5': 'Vimannagar'
    }
    while True:
        main_menu()
        choice = input("Select a branch: ")
        if choice in branches:
            branch_menu(branches[choice])
        elif choice == '6':
            print("Thank you for visiting Royal Palace. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

main()
