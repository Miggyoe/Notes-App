
print("search pad")
def search():
    notes = [
  "kangkong ni ethan",
  "Dr.maun strange",
  "ethansilog",
  "adrian pogi"
]

def search():
   keyword = input("search note:").lower()
   result =[note for note in notes if keyword in note.lower()]
   if result:
       print("\nSearch result:")
       for note in result:
           print("-", note)

       else:
           print("no note were found")
           search()

print(search())