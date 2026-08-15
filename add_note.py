notes = []

def add_note():
    title = input("Add note title: ")
    content = input("Add note text: ")
    if title:
        notes.append({"title": title, "content": content})
    print(f"Note {title} has been added!")

print(add_note())

def view_notes():
    if not notes:
        print("\nNo notes available...")
        return
    
    print("\nYour notes")
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note['title']}")
        print(f"{note['content']}\n")

print(view_notes())