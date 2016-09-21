from Tkinter import *
import passman


def edit(e):
    print "edit action"


def create(e):
    clearView()
    renderCreateView()
    print "create action"


def clearView():
    for widget in root.winfo_children():
        widget.destroy()


def renderListView():
    button1 = Button(root, text="Create")
    button1.grid(row=1, column=3, sticky=E)
    button1.bind("<Button-1>", create)

    button2 = Button(root, text="Edit")
    button2.grid(row=0, column=3, sticky=E)
    button2.bind('<Button-1>', edit)

    entries_list = Listbox(root, width=125, height=40, bd=0)
    entries_list.grid(row=0, column=0, columnspan=3, rowspan=10)

    if passman.entries != []:
        for entry in passman.entries:

            entries_list.insert(END, entry.toString())
    else:
        entries_list.insert(END, "No entries found!")


def renderCreateView():
    allow_uppercase = IntVar()
    allow_lowercase = IntVar()
    allow_numbers = IntVar()
    allow_special = IntVar()

    # Generate password button callback
    def btn_GenPass():
        length = len_e.get()
        if length:
            try:
                length = int(length)
                error_lbl.configure(text="")
                len_e.configure(highlightbackground=None)
            except:
                error_lbl.configure(text="Please enter a number.")
                len_e.configure(highlightbackground="red")

        allowed_classes = []
        if allow_uppercase.get() == 1: allowed_classes.append(0)
        if allow_lowercase.get() == 1: allowed_classes.append(1)
        if allow_numbers.get() == 1: allowed_classes.append(2)
        if allow_special.get() == 1: allowed_classes.append(3)

        pw = passman.generatePassword(allowed_classes, length)

        password_e.delete(0, END)
        password_e.insert(0, pw)

    def btn_GoBack():
        clearView()
        renderListView()

    fr = Frame(root, padx=20, pady=20)
    fr.grid(row=0, column=0)

    # Create and position labels
    Label(fr, text="Website: ").grid(row=0, sticky=W)
    Label(fr, text="Username: ").grid(row=1, sticky=W)
    Label(fr, text="Password: ").grid(row=2, sticky=W)
    Label(fr, text="Password Length: ").grid(row=3, sticky=W)
    Label(fr, text="Allowed Characters: ").grid(row=4, sticky=W)
    error_lbl = Label(fr, text="", fg="red")
    error_lbl.grid(row=8, column=0, columnspan=3)

    # Create widgets
    website_e = Entry(fr)
    username_e = Entry(fr)
    password_e = Entry(fr)
    len_e = Entry(fr)

    uppercase_chk = Checkbutton(fr, text="Uppercase letters (A-Z)", variable=allow_uppercase)
    lowercase_chk = Checkbutton(fr, text="Lowercase letters (a-z)", variable=allow_lowercase)
    numbers_chk = Checkbutton(fr, text="Numbers (0-9)", variable=allow_numbers)
    special_chk = Checkbutton(fr, text="Special characters (!$%@#)", variable=allow_special)

    create_btn = Button(fr, text="Create")
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

    create_btn.grid(row=8, column=2, sticky=W)
    generate_btn.grid(row=8, column=1, sticky=E)
    back_btn.grid(row=8, column=0, sticky=W)



root = Tk()

passman.loadList()

root.title("Passman!")
root.maxsize(1024, 768)
root.minsize(1024, 768)

renderCreateView()

root.mainloop()