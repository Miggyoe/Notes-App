def add_note(notes):
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