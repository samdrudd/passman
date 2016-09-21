import random
import atexit
import json
import string
from Tkinter import *

character_classes = [string.ascii_uppercase, string.ascii_lowercase, string.digits, '!$%@#']
entries = []


def generatePassword(allowed_classes, length):
    pw = ""
    for x in xrange(length):
        char_class = int(random.choice(allowed_classes))
        char = random.choice(character_classes[char_class])
        pw += str(char)
    return pw


def loadList():
    f = open("pw.txt", "r")
    if f:
        for line in f:
            entry = json.loads(line)
            entries.append(entry)
    f.close()


@atexit.register
def saveList():
    f = open("pw.txt", "r+")
    for entry in entries:
        f.write(json.dumps(entry) + '\n')
    f.close()


def clearView():
    for widget in root.winfo_children():
        widget.destroy()


def renderListView():

    def btn_Create():
        clearView()
        renderCreateView()

    def btn_Edit():
        try:
            ind = int(entries_list.curselection()[0])
        except:
            return
        clearView()
        renderCreateView(index=ind)

    def btn_CopyPassword():
        print "copying password"

    buttonframe = Frame(root)

    button1 = Button(buttonframe, text="Create New Entry", command=btn_Create)
    button1.pack(fill=X, ipadx=10)

    button2 = Button(buttonframe, text="Edit Selected Entry", command=btn_Edit)
    button2.pack(fill=X, pady=2)

    button3 = Button(buttonframe, text="Copy Selected Password", command=btn_CopyPassword)
    button3.pack(fill=X, pady=2)

    entries_list = Listbox(root, width=35, bd=0)
    entries_list.pack(side=LEFT, padx=5, pady=5, ipadx=5, ipady=5, fill=Y)
    buttonframe.pack(side=LEFT, padx=5, pady=5, fill=X, anchor='n')

    if entries:
        for x in xrange(len(entries)):
            entries_list.insert(x, entries[x]['website'])
    else:
        entries_list.insert(END, "No entries found!")


def renderCreateView(index=None):
    allow_uppercase = IntVar()
    allow_lowercase = IntVar()
    allow_numbers = IntVar()
    allow_special = IntVar()

    def btn_GoBack():
        clearView()
        renderListView()

    # Generate password button callback
    def btn_GenPass():
        length = len_e.get()
        if length:
            try:
                length = int(length)
            except:
                return
        else:
            return

        allowed_classes = []
        if allow_uppercase.get() == 1: allowed_classes.append(0)
        if allow_lowercase.get() == 1: allowed_classes.append(1)
        if allow_numbers.get() == 1: allowed_classes.append(2)
        if allow_special.get() == 1: allowed_classes.append(3)

        pw = generatePassword(allowed_classes, length)

        password_e.delete(0, END)
        password_e.insert(0, pw)

    def btn_Create():
        website = website_e.get()
        username = username_e.get()
        password = password_e.get()

        if website == "" or username == "" or password == "":
            return

        if index >= 0:
            entries[index]['website'] = website
            entries[index]['username'] = username
            entries[index]['password'] = password
        else:
            ent = {'website': website, 'username': username, 'password': password}
            entries.append(ent)

        btn_GoBack()

    fr = Frame(root, padx=20, pady=20)
    fr.pack()

    # Create and position labels
    Label(fr, text="Website: ").grid(row=0, sticky=W)
    Label(fr, text="Username: ").grid(row=1, sticky=W)
    Label(fr, text="Password: ").grid(row=2, sticky=W)
    Label(fr, text="Password Length: ").grid(row=3, sticky=W)
    Label(fr, text="Allowed Characters: ").grid(row=4, sticky=W)

    # Create widgets
    website_e = Entry(fr, width=30)
    username_e = Entry(fr, width=30)
    password_e = Entry(fr, width=30)
    len_e = Spinbox(fr, width=5, to=99)

    if index >= 0:
        website_e.insert(END, entries[index]['website'])
        username_e.insert(END, entries[index]['username'])
        password_e.insert(END, entries[index]['password'])
        len_e.insert(END, len(entries[index]['password']))
    else:
        len_e.insert(END, "10")

    website_e.focus()

    uppercase_chk = Checkbutton(fr, text="Uppercase letters (A-Z)", variable=allow_uppercase)
    lowercase_chk = Checkbutton(fr, text="Lowercase letters (a-z)", variable=allow_lowercase)
    numbers_chk = Checkbutton(fr, text="Numbers (0-9)", variable=allow_numbers)
    special_chk = Checkbutton(fr, text="Special characters (!$%@#)", variable=allow_special)

    create_btn_text = "Create"
    if index >= 0:
        create_btn_text = "Edit"

    create_btn = Button(fr, text=create_btn_text, command=btn_Create)
    generate_btn = Button(fr, text="Generate Password", command=btn_GenPass)
    back_btn = Button(fr, text="Back", command=btn_GoBack)

    # Position widgets
    website_e.grid(row=0, column=1, sticky=W)
    username_e.grid(row=1, column=1, sticky=W)
    password_e.grid(row=2, column=1, sticky=W)
    len_e.grid(row=3, column=1, sticky=W)

    uppercase_chk.grid(row=4, column=1, sticky=W)
    lowercase_chk.grid(row=5, column=1, sticky=W)
    numbers_chk.grid(row=6, column=1, sticky=W)
    special_chk.grid(row=7, column=1, sticky=W)

    create_btn.grid(row=8, column=1, sticky=E)
    generate_btn.grid(row=8, column=1, padx=50)
    back_btn.grid(row=8, column=0, sticky=W)


root = Tk()

loadList()

root.title("PassMan")
root.maxsize(400, 225)
root.minsize(400, 225)

renderListView()

root.mainloop()
