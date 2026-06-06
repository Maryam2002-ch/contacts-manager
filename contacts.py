import json

file_name = 'contact.json'

def load_contacts():
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    with open(file_name, 'w') as f:
        json.dump(contacts, f)

def show_contact():
    contacts = load_contacts()
    if contacts:
        print("\n📞 Your contacts:")
        for contact, number in contacts.items():
            print(f"  • {contact}: {number}")
    else:
        print("\n📭 Your contacts list is empty.")

def add_contact():
    contacts = load_contacts()
    
    while True:
        contacts_name = input("\nName of contact: ").strip()
        if not contacts_name:
            print("❌ Please fill the blank.")
            continue

        contacts_number = input("Number of contact: ").strip()
        if not contacts_number:
            print("❌ Please fill the blank.")
            continue
        
        contacts[contacts_name] = contacts_number
        save_contacts(contacts)
        print(f"\n✅ '{contacts_name}' added successfully.")
        return

def delete_contact():
    contacts = load_contacts()
    if not contacts:
        print("\n📭 Your contacts list is empty.")
        return
    
    delete_name = input("\nEnter the name of the contact you want to delete: ").strip()
    if delete_name in contacts:
        del contacts[delete_name]
        save_contacts(contacts)
        print(f"\n✅ '{delete_name}' deleted successfully.")
    else:
        print(f"\n❌ '{delete_name}' doesn't exist.")

def change_contact():
    contacts = load_contacts()
    if not contacts:
        print("\n📭 Your contacts list is empty.")
        return
    
    old_name = input("\nEnter the contact's name you want to change: ").strip()
    if old_name in contacts:
        new_name = input("New name for contact: ").strip()
        new_number = input(f"New number for '{new_name}': ").strip()
        
        del contacts[old_name]
        contacts[new_name] = new_number
        save_contacts(contacts)
        print(f"\n✅ Contact changed successfully from '{old_name}' to '{new_name}'.")
    else:
        print(f"\n❌ '{old_name}' doesn't exist.")
    
def reset_contacts():
    answer = input("\n⚠️ Are you sure? This will delete ALL your contacts. (yes/no): ").strip().lower()
    if answer == 'yes':
        save_contacts({})
        print("\n✅ All contacts have been deleted.")
    elif answer == 'no':
        print("\nReset cancelled.")
    else:
        print("\n❌ Please enter 'yes' or 'no'.")