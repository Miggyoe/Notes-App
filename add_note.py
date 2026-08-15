notes = []

def add_note():
    title = input("Add note title: ")
    content = input("Add note text: ")
    if title:
        notes.append({"title": title, "content": content})
    print(f"Note {title} has been added!")

print(add_note())