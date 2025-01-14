import sqlite3 as sql
from prompt_toolkit.shortcuts import button_dialog
from prompt_toolkit import print_formatted_text as print
from getch import getch

def paginate(lst) -> list:
    
    if type(lst) != list:
        raise ValueError
    paginated_list = []
    num = 5
    i = 1
    page = []
    for elem in lst:
        page.append(elem)
        if i < num:
            i += 1
        else:
            paginated_list.append(page)
            i = 1
            page = []
    if page:
        paginated_list.append(page)
    return paginated_list

def preppage(pageno : int, lst: list) -> list:
    if type(lst[pageno]) != list:
        raise TypeError
    page = lst[pageno]
    
    if pageno > 0:
        page = [("Prev",b'K')] + page
    if pageno < len(lst) - 1:
        page = page + [("Next",b'M')]
    page = page + [("Quit",None)]

    return page
    

class DiaryDB():
    
    def __init__(self):
        pass

    def initialize_DB(self):
        with sql.connect("DiaryEntries.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""
                create table if not exists entries (
                    id integer primary key autoincrement,
                    date text not null unique,
                    content text not null
                );
            """)
    
    def diary_fetch(self, date : str) -> str:
        with sql.connect("DiaryEntries.db") as connection:
            cursor = connection.cursor()
            cursor.execute("select content from entries where date = ?;",(date,))
            result = cursor.fetchone()
            return result[0] if result else None
    
    def diary_add(self, date : str, content : str) -> None:
        with sql.connect("DiaryEntries.db") as connection:
            cursor = connection.cursor()
            cursor.execute("select 1 from entries where date = ? limit 1;",(date,))
            result = cursor.fetchone()
            if not result:
                cursor.execute(
                    "insert into entries (date, content) values (?,?);",
                    (date,content,)
                )
                connection.commit()
            else:
                cursor.execute(
                    "update entries set content = ? where date = ?;",
                    (content,date,)
                )
                connection.commit()
            return None
        
    def diary_remove(self, date: str) -> None:
        with sql.connect("DiaryEntries.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "delete from entries where date = ?;",
            (date,))
            connection.commit()
            return None
        
    def diary_choose_one(self) -> str:
        with sql.connect("DiaryEntries.db") as connection:
            cursor = connection.cursor()
            lst = paginate([entry for entry in cursor.execute("select date, date from entries")])
            pageno = 0
            if not lst:
                result = button_dialog(
                    title="Oops!",
                    text="No Entries currently. Please press Enter to continue...",
                    buttons=[("OK", None)],
                ).run()

                return None
            
            while True:
                
                page = preppage(pageno,lst)

                result = button_dialog(
                    title=f"Choose Your Entry... ({pageno+1}/{len(lst)})",
                    text="Please Choose One of the below Options...",
                    buttons=page,
                ).run()
                
                if result:
                    if result == b'M':
                        pageno += 1 if pageno < len(lst) else None
                    elif result == b'K':
                        pageno -= 1 if pageno > 0 else None
                    else:
                        return result
                
                else:
                    return None

if __name__ == "__main__":
    pass