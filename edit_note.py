# Adrian
notes = []

def edit_note():
    selected = note_list.curselection()
    
    if selected:
        index = slected[0]
        notes[index] = text_area.get("1.0", "end").strip()
        update_list()


