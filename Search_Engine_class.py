from tkinter import *
from tkinter import filedialog


class Search_Engine():
    def __init__(self):
        root.bind('<Return>', self.bin)
        root.bind_all("<Key>", self._onKeyRelease, "+")
        self.label = Label()
        self.label.grid()
        self.name_label = Label(text="Введите ник:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.path = Text(root, width=100, height=20, bg='beige', font="Times 12")
        self.path.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.pathlabel = Label(font="Times 11")
        self.pathlabel.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = Entry(width=50, bg='beige')
        self.name_entry.grid(row=0, column=0, padx=5, pady=5)

        self.btn = Button(root, text='Очистить Лог Файл', background="#555", foreground="#ccc", command=self.qwe)
        self.btn.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.display_button = Button(text="Поиск", background="#555", foreground="#ccc", command=self.display)
        self.display_button.grid(row=2, column=0, padx=250, pady=5, sticky="w")
        self.clear_button = Button(text="Очистить", background="#555", foreground="#ccc", command=self.clear)
        self.clear_button.grid(row=2, column=0, padx=350, pady=5, sticky="w")
        self.browsebutton = Button(root, text="Загрузить Лог Файл", background="#555", foreground="#ccc",
                                   command=self.browsefunc)
        self.browsebutton.grid(row=5, column=0, padx=5, pady=5, sticky="e")

    def browsefunc(self):
        global f
        global fread
        global filename
        filename = filedialog.askopenfilename()
        self.pathlabel.config(text=filename)
        self.f = open(filename, "r", encoding='utf-8')
        fread = f.readlines()

    def display(self):
        f = open(filename, "r", encoding='utf-8')
        fread = f.readlines()
        for line in fread:
            if not self.name_entry.get():
                break
            if self.name_entry.get() in line:
                self.path.insert(1.0, line)

    def qwe(self):
        with open(filename, "r", encoding='utf-8') as file:
            lines = file.readlines()
        del lines
        with open(filename, "w", encoding='utf-8') as file:
            file.writelines(lines)

    def clear(self):
        self.name_entry.delete(0, END)
        self.path.delete(1.0, END)

    def bin(self, event):
        self.display()

    def _onKeyRelease(self, event):
        ctrl = (event.state & 0x4) != 0
        if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
            event.widget.event_generate("<<Cut>>")

        if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
            event.widget.event_generate("<<Paste>>")

        if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
            event.widget.event_generate("<<Copy>>")


if __name__ == '__main__':
    root = Tk()
    app = Search_Engine()
    root.title("Поисковик 0.1")
    root.resizable(width=False, height=False)
    root.mainloop()
