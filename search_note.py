# print("search pad")
# def search(notes):
#     notes = [
#   "kangkong ni ethan",
#   "Dr.maun strange",
#   "ethansilog",
#   "adrian pogi"
# ]

def search(notes):
   keyword = input("search note: ").lower()
   result = [note for note in notes if keyword in note['title'].lower() or keyword in note['content'].lower()]
   if result:
       print("\nSearch result:")
       for note in result:
           print("-", note)
           break
       else:
           print("no note were found")
           
