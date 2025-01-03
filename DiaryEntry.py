from prompt_toolkit import prompt, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import yes_no_dialog
from datetime import datetime


class DiaryEntry():
    now = datetime.now()

    def __init__(self, date_of_entry = now.strftime("%d-%m-%Y"), contents_of_entry = ""):
        self.date_of_entry = date_of_entry
        self.contents_of_entry = contents_of_entry

    def prompt_entry(self) -> None:
        """Prompts user for entry. Useful for both editing and creating a new entry."""
        style = Style.from_dict({
            'comp' : '#ff0066',
            'date' : '#44ff00 italic',
            'shortcut' : '#0563fa bold italic'
        })

        while True:
            self.contents_of_entry = prompt(
                HTML(f"<comp>Entry Date:--</comp> <date>{self.date_of_entry}</date>\n",),
                style=style,
                default=self.contents_of_entry,
                multiline=True,
                bottom_toolbar=HTML("To Confirm, Please press <shortcut>'Esc + Enter'</shortcut>")
            )
            
            result = yes_no_dialog(
                title="Are you sure?",
                text="Would you like to save your input?"
            ).run()
            
            if result:
                """Save to DB using `SQLite3` library. Will place code in once I'm done with that.
                For now, here's a print statement as a proof of concept."""
                print(f"This is the entry for the date {self.date_of_entry}:\n{self.contents_of_entry}")
                break
            
            return None
            

    def display_entry(self) -> None:
        """Displays current entry in read-only mode."""
        print(self.contents_of_entry)
        return None