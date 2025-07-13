contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"Contact '{name}' added successfully!\n")

def view_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}\n")
    else:
        print("Contact not found!\n")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep old value):")
        phone = input("New phone number: ")
        email = input("New email: ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        print(f"Contact '{name}' updated!\n")
    else:
        print("Contact not found!\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.\n")
    else:
        print("Contact not found!\n")

def show_all_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")
    print()

# Main Menu
while True:
    print("=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        show_all_contacts()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!\n")

  
