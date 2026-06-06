from contacts import show_contact, add_contact, delete_contact, change_contact, reset_contacts

with open('contact.json', 'a') as c_object:
    pass

while True:
    choose = input("\nThis is contacts program. Choose one: ('Show', 'Add', 'Delete', 'Change', 'Reset','Quit'): ").strip().title()
    if choose == 'Show':
        show_contact()
        continue
    elif choose == 'Add':
        add_contact()
        continue
    elif choose == 'Delete':
        delete_contact()
        continue
    elif choose == 'Change':
        change_contact()
        continue
    elif choose == 'Quit':
        print("\nYou quited the program.")
        break
    elif choose == 'Reset':
        reset_contacts()
        continue
    else:
        print("\nPlease choose a valid choice.")
        continue

