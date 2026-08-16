notes = []

def add_note():
    title = input("Add note title: ")
    content = input("Add note text: ")
    if title:
        notes.append({"title": title, "content": content})
        print(f"\nNote '{title}' has been added!\n")
    else:
        print("Title cannot be empty!\n")

def view_notes():
    if not notes:
        print("\nNo notes available...\n")
        return

    print("\n--- Your Notes ---")
    count = 1

    for note in notes:
        print(f"{count}. {note['title']}")
        print(f"   - {note['content']}")
        count += 1
    print()

def main():
    while True:
        print("--- Notes App ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()