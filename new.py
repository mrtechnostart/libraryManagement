import sqlite3
conn = sqlite3.connect("library.db")
c = conn.cursor()
def isBookRec(BookName,BookCode):
    c.execute('select * from bookRec')
    data = c.fetchall()
    for i in data:
        if i[0] == BookName and i[1] == BookCode:
            return True
        else:
            return False
print(isBookRec('',''))