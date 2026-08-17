# notes = []

# from notes import notes

def delete_note(notes):
    if not notes:
        print(30*"=")
        print("No notes available...")
        print(30*"=")
        return
    print(30*"=")
    print("---Your Notes---")
    print(30*"=")

    count = 1
    for note in notes:
        print(f"{count}. {note['title']}")
        print(30*"=")
        count += 1
    
    print(30*"=")
    choice = int(input("Select note to delete: "))
    print(30*"=")

    if choice >= 1 and choice <= len(notes):
        notes.pop(choice - 1)
        print(30*"=")
        print("Note deleted!")
        print(30*"=")
    else:
        print(30*"=")
        print("Invalid note.")
        print(30*"=")