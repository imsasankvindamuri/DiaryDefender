from prompt_toolkit import prompt, print_formatted_text as print, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import yes_no_dialog
from datetime import datetime
import os

class DiaryIO():
    
    def __init__(self, date_of_entry : str = None, contents_of_entry : str = ""):
        now = datetime.now()
        self.date_of_entry = date_of_entry or now.strftime("%d-%m-%Y")
        self.contents_of_entry = contents_of_entry

    def prompt_entry(self) -> None:
        """Prompts user for entry. Useful for both editing and creating a new entry."""
        
        style = Style.from_dict({
            'diaryprompt' : '#ff0066',
            'date' : '#44ff00 italic',
            'shortcut' : '#0563fa bold italic'
        })

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.contents_of_entry = prompt(
                HTML(f"<diaryprompt>Entry Date:--</diaryprompt> <date>{self.date_of_entry}</date>\n",),
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
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print(
                    HTML(f"<diaryprompt>This is the entry for the date</diaryprompt> <date>{self.date_of_entry}:</date>\n{self.contents_of_entry}"),
                    style=style
                )
                return None
            

    def display_entry(self) -> None:
        pass


    
if __name__ == "__main__":
    pass