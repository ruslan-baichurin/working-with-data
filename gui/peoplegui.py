"""
Implement a GUI for viewing and updating class instances
stored in a shelve;
the shelve lives on the machine this script runs on, as
one or more local files;
"""

from tkinter import *
from tkinter.messagebox import showerror
import shelve

shelve_name = 'class_shelve'
field_names = ('name', 'age', 'job', 'pay')


def make_widgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + field_names):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text='Fetch', command=fetch_record).pack(side=LEFT)
    Button(window, text='Update', command=update_record).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)

    return window


def fetch_record():
    key = entries['key'].get()
    try:
        record = db[key]  # fetch by key, show in GUI
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in field_names:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def update_record():
    key = entries['key'].get()
    if key in db:
        record = db[key]  # update existing record
    else:
        from cli.person import Person  # make/store new one for key
        record = Person(name='?', age='?')
    for field in field_names:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record


db = shelve.open(shelve_name)
window = make_widgets()
window.mainloop()
db.close()
