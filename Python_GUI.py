from Tkinter import *


def strip_id(str):
    search_string = "/prospects/"
    index = str.find(search_string)
    id_index = index + len(search_string)
    trimmed_string = str[id_index:]
    index_2 = trimmed_string.find("/")
    trimmed_string_2 = trimmed_string[:index_2]
    return trimmed_string_2

master = Tk()
master.wm_attributes("-topmost", 1)
master.wm_title("Outreach")

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    entry = e.get()
    print strip_id(entry)

b = Button(master, text="Submit", width=10, command=callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)
