import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox


def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text files", "*.txt")])
    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as file:
        content = file.read()
        text_edit.insert(tk.END, content)
    window.title(f"Text Editor - {filepath}")


def save_file(window, text_edit):
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not filepath:
        return
    with open(filepath, "w") as file:
        content = text_edit.get(1.0, tk.END)
        file.write(content)
    window.title(f"Text Editor - {filepath}")


def count_lines_words(text_edit):
    content = text_edit.get(1.0, tk.END)
    lines = len(content.split("\n"))
    words = len(content.split())
    messagebox.showinfo("Word and Line Count", f"Total Lines: {lines}\nTotal Words: {words}")


def change_font(text_edit, font_family, font_size):
    text_edit.config(font=(font_family, font_size))


def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.geometry("600x400")
    window.minsize(500, 400)

    text_edit = tk.Text(window, font=("Arial", 14))
    text_edit.pack(expand=True, fill="both")

    menu_bar = tk.Menu(window)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=lambda: open_file(window, text_edit))
    file_menu.add_command(label="Save", command=lambda: save_file(window, text_edit))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Word/Line Count", command=lambda: count_lines_words(text_edit))
    edit_menu.add_separator()
    edit_menu.add_command(label="Change Font", command=lambda: change_font(text_edit, "Courier", 16))
    edit_menu.add_command(label="Reset Font", command=lambda: change_font(text_edit, "Arial", 14))
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    window.config(menu=menu_bar)
    window.mainloop()


main()
