notes = []

def add_note():
    title = input("Add note title: ")
    content = input("Add note text: ")
    notes[title] = content
    print(f"Note {title} has been added!")

print(add_note())