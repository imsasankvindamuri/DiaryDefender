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

if __name__ == "__main__":
    pass