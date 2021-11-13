from tkinter import *
from tkinter import filedialog


def browsefunc():
    global f
    global fread
    global filename
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    f = open(filename, "r", encoding='utf-8')
    fread = f.readlines()


def display():
    f = open(filename, "r", encoding='utf-8')
    fread = f.readlines()
    for line in fread:
        if not name_entry.get():
            break
        if name_entry.get() in line:
            path.insert(1.0, line)  # messagebox.showinfo("Найден ник", line)


def qwe():
    with open(filename, "r", encoding='utf-8') as file:
        lines = file.readlines()
    del lines
    with open(filename, "w", encoding='utf-8') as file:
        file.writelines(lines)


def clear():
    name_entry.delete(0, END)
    path.delete(1.0, END)


def _onKeyRelease(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")

    if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")

    if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")


def bin(event):
    display()


root = Tk()
root.title("Поисковик 0.1")
btn = Button(root, text='Очистить Лог Файл', background="#555", foreground="#ccc", command=qwe)
btn.grid(row=2, column=0, padx=5, pady=5, sticky="w")
root.resizable(width=False, height=False)
name_label = Label(text="Введите ник:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = Entry(width=50, bg='beige')
name_entry.grid(row=0, column=0, padx=5, pady=5)
message = StringVar()
display_button = Button(text="Поиск", background="#555", foreground="#ccc", command=display)
display_button.grid(row=2, column=0, padx=250, pady=5, sticky="w")
root.bind('<Return>', bin)
clear_button = Button(text="Очистить", background="#555", foreground="#ccc", command=clear)
clear_button.grid(row=2, column=0, padx=350, pady=5, sticky="w")
browsebutton = Button(root, text="Загрузить Лог Файл", background="#555", foreground="#ccc", command=browsefunc)
browsebutton.grid(row=2, column=0, padx=5, pady=5, sticky="e")
root.bind_all("<Key>", _onKeyRelease, "+")
label = Label()
label.grid()
path = Text(root, width=100, height=20, bg='beige', font="Times 12")
path.grid(row=7, column=0, padx=5, pady=5, sticky="w")
pathlabel = Label(font="Times 11")
pathlabel.grid(row=6, column=0, padx=5, pady=5, sticky="w")

root.mainloop()
