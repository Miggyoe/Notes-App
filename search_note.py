# print("search pad")
# def search(notes):
#     notes = [
#   "kangkong ni ethan",
#   "Dr.maun strange",
#   "ethansilog",
#   "adrian pogi"
# ]

def search_note(notes):
    print("="*30)
    keyword = input("search note: ").lower()
    print("="*30)
    result = [note for note in notes if keyword in note['title'].lower() or keyword in note['content'].lower()]
    if result:
        print("="*30)
        print("\nSearch result:")
        print("="*30)
        for note in result:
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            print("="*30)    
    else:
        print("No note were found...")
        print("="*30)
