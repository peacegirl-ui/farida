print("WELCOME MENU")
print("Please select an option:")

print("1.Add a New Entry")
print("2.View all Entries")
print("Search for an Entry")
print("Delete All Entry")
print("Exit")

journal_entries = []

def show_menu():
    print("\n--- Personal Journal Manager ---")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete an Entry")
    print("5. Exit")

def add_entry():
    entry = input("Enter your journal entry: ")
    journal_entries.append(entry)
    print("✅ Entry added successfully!")

def view_entries():
    if not journal_entries:
        print("No entries found.")
    else:
        print("\n--- All Journal Entries ---")
        for i, entry in enumerate(journal_entries, start=1):
            print(f"{i}. {entry}")

def search_entry():
    keyword = input("Enter keyword to search: ")
    found = False
    for i, entry in enumerate(journal_entries, start=1):
        if keyword.lower() in entry.lower():
            print(f"{i}. {entry}")
            found = True
    if not found:
        print("No matching entries found.")

def delete_entry():
    view_entries()
    try:
        index = int(input("Enter entry number to delete: "))
        if 1 <= index <= len(journal_entries):
            removed = journal_entries.pop(index - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        search_entry()
    elif choice == '4':
        delete_entry()
    elif choice == '5':
        print(" Exiting Journal Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again from above menu"
        ".")



