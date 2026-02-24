import json
import os

FILENAME = "contacts.json"

# Loading contacts from file
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Saving contacts to file
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=2)

# Adding new contact
def add_contact(contacts):
    print("\n--- Add Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email (optional): ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully")

# Viewing all contacts
def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

# Searching contact
def search_contact(contacts):
    search = input("\nEnter name to search: ").lower()
    found = False

    for contact in contacts:
        if search in contact["name"].lower():
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True

    if not found:
        print("No contact found.")

# Deleting contact
def delete_contact(contacts):
    view_contacts(contacts)
    number = int(input("\nEnter contact number to delete: ")) - 1

    if 0 <= number < len(contacts):
        contacts.pop(number)
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Invalid number.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n====== Contact Book ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()