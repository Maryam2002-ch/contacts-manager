# 📞 Contacts Manager

A simple command-line contact manager written in Python that stores your contacts in a JSON file. Your contacts are saved between program runs!

## ✨Features

- ✅ Add new contacts
- ✅ View all contacts
- ✅ Delete existing contacts
- ✅ Change contact name or number
- ✅ Reset all contacts (with confirmation)
- ✅ Data persists using JSON file
- ✅ Input validation and error handling

## 📁 Project Structure

contacts-manager/
├── contacts.py      # Main logic (add, delete, change, show, reset)
├── main.py          # User interface and menu
└── contact.json     # Your contacts are saved here (auto-generated)

## 🚀 How to Run

1. Make sure you have Python installed (version 3.6+)
2. Open terminal in the project folder
3. Run this command:

python main.py

## 🎮 How to Use

When you run the program, you'll see a menu:

Options: Show, Add, Delete, Change, Reset, Quit

- Show → Display all saved contacts
- Add → Add a new contact (name and number)
- Delete → Remove a contact by name
- Change → Edit an existing contact's name or number
- Reset → Delete ALL contacts (asks for confirmation)
- Quit → Exit the program

## 📝 Example

Choose: Add
Name of contact: Sara
Number of contact: 09123456789

✅Contact added successfully.

Choose: Show

📞 Your contacts:
Sara: 09123456789

## 🛠️ Code Highlights

- Uses json module for persistent storage
- Modular functions for each operation
- Error handling for empty JSON files
- Separate files for logic (contacts.py) and interface (main.py)

## 🔜 Future Improvements

- Search contacts by name
- Edit individual fields
- Export/import contacts from CSV
- Phone number validation

## 📄 License

Feel free to use, modify, and share this project for learning purposes.

---

⭐ If you found this project helpful, give it a star!
