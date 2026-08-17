from add_note import add_note
from view_note import view_note
from edit_note import edit_note
from search_note import search_note

def main():
    notes = []

    while True:
        print(30*"=")
        print("---Options---")
        print("1. Add note")
        print("2. View note")
        print("3. Edit note")
        print("4. Search note")
        print("5. Delete note")
        print("6. Exit")
        choice = input("Select an option (1/2/3/4/5/6): ")
        print(30*"=")
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_note(notes)
        elif choice == "3":
            edit_note(notes)
        elif choice == "4":
            search_note(notes)
        elif choice == "5":
            delete_note(notes)
        elif choice == "6":
            print(30*"=")
            print("Goodbye!")
            print(30*"=")
            break
        else:
            print(30*"=")
            print("Invalid.")
            print(30*"=")

if __name__ == "__main__":
    main()