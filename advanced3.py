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


def search_replace(text_edit, search_text, replace_text):
    content = text_edit.get(1.0, tk.END)
    updated_content = content.replace(search_text, replace_text)
    text_edit.delete(1.0, tk.END)
    text_edit.insert(tk.END, updated_content)


def undo(text_edit):
    try:
        text_edit.edit_undo()
    except tk.TclError:
        pass


def redo(text_edit):
    try:
        text_edit.edit_redo()
    except tk.TclError:
        pass


def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.geometry("600x400")
    window.minsize(500, 400)

    text_edit = tk.Text(window, font=("Arial", 14))
    text_edit.pack(expand=True, fill="both")

    menu_bar = tk.Menu(window)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=lambda: open_file(window, text_edit), accelerator="Ctrl+O")
    file_menu.add_command(label="Save", command=lambda: save_file(window, text_edit), accelerator="Ctrl+S")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Word/Line Count", command=lambda: count_lines_words(text_edit))
    edit_menu.add_separator()
    edit_menu.add_command(label="Change Font", command=lambda: change_font(text_edit, "Courier", 16))
    edit_menu.add_command(label="Reset Font", command=lambda: change_font(text_edit, "Arial", 14))
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo", command=lambda: undo(text_edit), accelerator="Ctrl+Z")
    edit_menu.add_command(label="Redo", command=lambda: redo(text_edit), accelerator="Ctrl+Y")
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    search_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Search", menu=search_menu)
    search_menu.add_command(label="Find and Replace", command=lambda: find_replace_window(window, text_edit))

    window.config(menu=menu_bar)

    # Bind keyboard shortcuts
    window.bind("<Control-z>", lambda event: undo(text_edit))
    window.bind("<Control-y>", lambda event: redo(text_edit))
    window.bind("<Control-o>", lambda event: open_file(window, text_edit))
    window.bind("<Control-s>", lambda event: save_file(window, text_edit))

    window.mainloop()


def find_replace_window(parent, text_edit):
    search_window = tk.Toplevel(parent)
    search_window.title("Find and Replace")

    search_label = tk.Label(search_window, text="Find:")
    replace_label = tk.Label(search_window, text="Replace:")
    search_entry = tk.Entry(search_window)
    replace_entry = tk.Entry(search_window)

    search_label.grid(row=0, column=0)
    replace_label.grid(row=1, column=0)
    search_entry.grid(row=0, column=1)
    replace_entry.grid(row=1, column=1)

    search_button = tk.Button(search_window, text="Search and Replace",
                              command=lambda: search_replace(text_edit, search_entry.get(), replace_entry.get()))
    search_button.grid(row=2, columnspan=2)


if __name__ == "__main__":
    main()
