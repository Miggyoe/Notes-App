notes = []

def add_note():
    print(30*"=")
    title = input("Enter note title: ")
    content = input("Enter note text: ")
    if title:
        notes.append({'title': title, 'content': content})
        print(30*"=")
        print(f"Note {title} has been added!")
        print(30*"=")
        return
    else:
        print(30*"=")
        print("Title cannot be empty.")
        print(30*"=")

def view_note():
    if not notes:
        print(30*"=")
        print("No notes available...")
        print(30*"=")
        return
    elif notes:
        print(30*"=")
        print("---Your Notes---")
        count = 1
        for note in notes:
            print(f"{count}. {note['title']}")
            print(f"   - {note['content']}")
            count += 1
        print(30*"=")

while True:
    print(30*"=")
    print("---Options---")
    print("1. Add note")
    print("2. View note")
    print("3. Exit")
    choice = input("Select an option (1/2/3): ")
    print(30*"=")
    if choice == "1":
        add_note()
    elif choice == "2":
        view_note()
    elif choice == "3":
        print(30*"=")
        print("Goodbye!")
        print(30*"=")
        break
    else:
        print(30*"=")
        print("Invalid.")
        print(30*"=")