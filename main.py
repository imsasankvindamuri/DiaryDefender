import os
from prompt_toolkit.shortcuts import button_dialog, yes_no_dialog
from DiaryDB import DiaryDB
from DiaryIO import DiaryIO

def add_entry(DiaryIO: DiaryIO, DiaryDB: DiaryDB) -> None:
    
    DiaryIO.prompt_entry()
    DiaryDB.diary_add(DiaryIO.date_of_entry,DiaryIO.contents_of_entry)
    os.system('cls' if os.name == 'nt' else 'clear')
    return None

def edit_existing_entry(DiaryIO: DiaryIO, DiaryDB: DiaryDB) -> None:
    
    date = DiaryDB.diary_choose_one()
    if date != None:
        DiaryIO.date_of_entry, DiaryIO.contents_of_entry = date, DiaryDB.diary_fetch(date)
        add_entry(DiaryIO, DiaryDB)
    return None

def delete_existing_entry(DiaryIO: DiaryIO, DiaryDB: DiaryDB):
    
    date = DiaryDB.diary_choose_one()
    if date != None:
        result = yes_no_dialog(
            title="Are you sure?",
            text=f"Are you sure you want to delete the entry dated {date}?"
        ).run()

        if result:
            DiaryDB.diary_remove(date)
            return None
        else:
            return None
    return None

def view_an_entry(DiaryIO: DiaryIO, DiaryDB: DiaryDB) -> None:
    
    date = DiaryDB.diary_choose_one()
    if date != None:
        DiaryIO.date_of_entry, DiaryIO.contents_of_entry = date, DiaryDB.diary_fetch(date)
        DiaryIO.display_entry()
    return None


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    newDiaryDB = DiaryDB()
    newDiaryIO = DiaryIO()

    newDiaryDB.initialize_DB()

    button_action_map = [
        ("Add New Entry", "Add New Entry"),
        ("Edit Existing Entry", "Edit Existing Entry"),
        ("Delete Existing Entry", "Delete Existing Entry"),
        ("View an Entry", "View an Entry"),
        ("Quit", False),
    ]

    action_function_map = {
        "Add New Entry" : add_entry,
        "Edit Existing Entry" : edit_existing_entry,
        "Delete Existing Entry" : delete_existing_entry,
        "View an Entry" : view_an_entry,
    }

    while True:

        result = button_dialog(
            title="DiaryDefender",
            text="Please Choose One Option:--",
            buttons=button_action_map,
        ).run()

        if result != False:

            action_function_map[result](DiaryIO=newDiaryIO, DiaryDB=newDiaryDB)

        else:
            confirm = yes_no_dialog(
                title="Are you sure?",
                text="Are you sure you want to quit?"
            ).run()

            if confirm:
                break