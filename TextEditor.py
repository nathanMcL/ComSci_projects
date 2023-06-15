import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="Choose a color")
    text_area.config(fg=color[1])
    print(color)

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("ALL Files", "*.*"),
                                                          ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")
        text_area.insert(1.0, file.read())

    except Exception:
        print("Error, reading file")

    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))

        except Exception:
            print("File was not saved")

        finally:
            file.close()


def cut():
    text_area.event_generate(("<<Cut>>"))

def copy():
    text_area.event_generate(("<<Copy>>"))

def paste():
    text_area.event_generate(("<<Paste>>"))

def about():
    showinfo("About this program", "Welcome to my Python Text Editor!  "
                                   " This program is a simple text editor that can be used to create, edit, and save text files. "
                                   " It is written in Python, and it is available for Windows, macOS, and Linux. "
                                   " Use with caution. ")

def quit():
    window.destroy()

#window
window = Tk()
window.title("Text editor program")
file = None

window_width = 600
window_height = 800

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width /2) - (window_width / 2))
y = int((screen_height /2) - (window_height / 2))

#window screen placement
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

#font default
font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("25")

#setting test area
text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

#color button
color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

#font button
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

#size button
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

#menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

#file menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

#edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

#help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()

