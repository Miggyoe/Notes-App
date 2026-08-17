# Adrian

def edit_note():
    if not notes:
        print(30*"=")
        print("No notes available..")
        print(30*"=")
        return

    view_note()

    choice = input("Select a note number to edit: ")

    if choice.isdigit():
        index = int(choice) - 1

        if 0 <= index < len(notes):
            print(30*"=")
            print(f"editing note:, {notes[index]["title"]}")

            title = input("enter new title: ")
            content = input("enter new note text: ")

            if title:
                notes[index]['title'] = title

            if content:
                notes[index]['content'] = content

            print(30*"=")
            print("Notes has been edited! ")
            print(30*"=")

        
         




