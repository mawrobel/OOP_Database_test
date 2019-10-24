import tkinter as tk
from tkinter.messagebox import showerror
import shelve

shelvename = "class-shelve"
fieldnames = ('name', 'age', 'pay', 'job')


def makeWidgets():
    global entries
    window = tk.Tk()
    window.title('People Shelve')
    form = tk.Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
       lab = tk.Label(form, text=label)
       ent = tk.Entry(form)
       lab.grid(row=ix, column=0)
       ent.grid(row=ix, column=1)
       entries[label] = ent
    tk.Button(window, text="Fetch", command=fetchRecord).pack(side="left")
    tk.Button(window, text="Update", command=updateRecord).pack(side="left")
    tk.Button(window, text="Quit", command=window.quit).pack(side="right")
    return window
def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key] # fetch by key, show in GUI
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, "end")
            entries[field].insert(0, repr(getattr(record, field)))
def updateRecord():
    key = entries['key'].get()
    if key in db:
       record = db[key] # update existing record
    else:
        from DataBase import Person # make/store new one for key
        record = Person(name='?', age='?') # eval: strings must be quoted
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

if __name__ == '__main__':
    db = shelve.open(shelvename)
    window = makeWidgets()
    window.mainloop()
    db.close()