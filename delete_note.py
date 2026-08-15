
notes = []

def delete_note
    selected = note list.curseselection()

    if selected:
        index = selected[0]
        notes[index] = text_area.get()



print(input)