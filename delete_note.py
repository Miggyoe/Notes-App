#unfinished
notes = []

def delete_notes():
    selected = note list.curseselection()

    if selected:
        index = selected[0]
        notes[index] = text_area.remove("1.0", "end").strip()
        update_list{}



