notes = []

from notes import notes


def delete_note():
    if not notes:
        print("No notes available...")
        return
    print("Your notes:")

    count = 1
        for note in notes:
        print(count, note["title"])
        count += 1
    
    choice = int(input("Select note to delete: "))

    if choice >= 1 and choice <= len(notes):
        notes.pop(choice - 1)
        print("Note deleted!")
    else:
        print("Invalid note.")