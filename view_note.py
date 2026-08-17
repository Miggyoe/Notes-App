def view_note(notes):
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