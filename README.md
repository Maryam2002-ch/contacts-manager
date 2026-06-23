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

## 🚀 How to Run

1. Make sure you have Python installed (version 3.6+)
2. Open terminal in the project folder
3. Run this command:

```bash
python main.py
```
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

Choose: Add <br>
Name of contact: Sara <br>
Number of contact: 09123456789

✅Contact added successfully.

Choose: Show

📞 Your contacts: <br>
Sara: 09123456789

## 🛠️ Code Highlights

- Uses json module for persistent storage
- Modular functions for each operation
- Error handling for empty JSON files
- Separate files for logic (contacts.py) and interface (main.py)

---

⭐ If you found this project helpful, give it a star!
