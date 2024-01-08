import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text files", "*.txt")])
    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")


def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text files", "*.txt")])
    if not filepath:
        return
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")


def main():
    window = tk.Tk()
    window.title("Text editor")

    # Set minimum size for window
    window.minsize(500, 400)

    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=0, sticky="nsew")  # Use sticky to expand the Text widget

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5)  # Added padding for better spacing
    open_button.grid(row=0, column=1, padx=5, pady=5)  # Positioned the buttons side by side

    frame.grid(row=1, column=0, pady=10)  # Positioned the frame with buttons below the Text widget

    # Configure grid weights to make the Text widget expandable
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()


main()
