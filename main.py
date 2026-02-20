import tkinter as tk
from tkinter import ttk, messagebox

from converter import text_to_morse, morse_to_text

# The Fucntion
def convert_action():
    user_input = input_text.get("1.0", tk.END).strip()

    if not user_input:
        set_status("⚠ Enter text to convert.")
        return
    
    mode = mode_var.get()

    try:
        if mode == "text_to_morse":
            result = text_to_morse(user_input)
        else:
            result = morse_to_text(user_input)

        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state="disabled")

        set_status("✓ Converted successfully")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_instructions():
    instruction_win = tk.Toplevel(root)
    instruction_win.title("How to Use MorsePy")
    instruction_win.geometry("540x420")
    instruction_win.resizable(False, False)

    frame = ttk.Frame(instruction_win, padding=15)
    frame.pack(fill="both", expand=True)

    text_widget = tk.Text(
        frame,
        wrap=tk.WORD,
        font=("Segoe UI", 10),
        relief=tk.FLAT,   
    )
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget.config(yscrollcommand=scrollbar.set)
    instructions = '''
Welcome to MorsePy – Morse Code Translator

1. Choose Conversion Mode
   • Text → Morse : converts normal text into Morse code
   • Morse → Text : converts Morse into English

2. Input Rules
   • For Morse input:
        0 = dot (.)
        1 = dash (-)
        space = letter separator
        / = word separator

   Example:
        0000 0 0100 0100 111 / 011 111 010 0100 100

3. Buttons
   • Convert → performs conversion
   • Clear → clears both boxes
   • Copy Output → copies result to clipboard

4. Font Size
   Use the dropdown to adjust readability.

5. Status Bar
   Shows feedback for actions performed.

Tip:
Start by typing a simple word like HELLO
to see how the translator works.
'''
    text_widget.insert("1.0", instructions)
    text_widget.config(state="disabled")


def clear_action():
    input_text.delete("1.0", tk.END)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")
    set_status("✓ Cleared input and output")

def copy_action():
    result = output_text.get("1.0", tk.END).strip()

    if not result:
        set_status("⚠ No output to copy.")
        return
    
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()

    set_status("✓ Output copied to clipboard")

def set_status(message):
    status_var.set(message)
    root.after(3000, lambda: status_var.set(""))  # Clear status after 3 seconds

def change_font_size(event=None):
    size = FONT_SIZE[font_size_var.get()]
    new_font = ("Consolas", size)
    input_text.config(font=new_font)
    output_text.config(font=new_font)
    set_status(f"✓ Font size changed to {font_size_var.get()}")


# Windows Creations
root = tk.Tk()
root.title("MorsePy")
root.geometry("640x500")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# Status Variable Setup
status_var = tk.StringVar(value="Ready")

FONT_SIZE = {
    "Small": 12,
    "Medium": 14,
    "Large": 16
}

TITLE_FONT = ("Segoe UI", 18, "bold")
LABEL_FONT = ("Segoe UI", 10)
BUTTON_FONT = ("Segoe UI", 10, "bold")
TEXT_FONT = ("Consolas", FONT_SIZE["Medium"])

title_label = ttk.Label(
    root,
    text="MorsePy - Morse Code Translator",
    font=TITLE_FONT,
)
title_label.pack(pady=5)

# Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="How to Use", command=show_instructions)
help_menu.add_separator()
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About MorsePy", "MorsePy v1.0\nCreated by SiddharthShah30\nA simple Morse code translator built with Python and Tkinter."))

# Status Bar
status_bar = ttk.Label(
    root,
    textvariable=status_var,
    relief=tk.SUNKEN,
    anchor="w",
    padding=5
)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Mode Variable Setup
mode_var = tk.StringVar(value="text_to_morse")

mode_frame = ttk.Frame(root)
mode_frame.pack(pady=5)

# Mode Selection
ttk.Radiobutton(
    mode_frame,
    text = "Text -> Morse",
    variable = mode_var,
    value = "text_to_morse"
).pack(side=tk.LEFT, padx=15)

ttk.Radiobutton(
    mode_frame,
    text = "Morse -> Text",
    variable = mode_var,
    value = "morse_to_text"
).pack(side=tk.LEFT, padx=15)

# Font Size Selection

font_frame = ttk.Frame(root)
font_frame.pack(pady=5)

ttk.Label(font_frame, text="Font Size:", font=LABEL_FONT).pack(side=tk.LEFT, padx=5)

font_size_var = tk.StringVar(value="Medium")

font_dropdown = ttk.Combobox(
    font_frame,
    textvariable=font_size_var,
    values=["Small", "Medium", "Large"],
    state="readonly",
    width=10,
)
font_dropdown.pack(side=tk.LEFT, padx=5)

font_dropdown.bind("<<ComboboxSelected>>", change_font_size)

# Input
ttk.Label(root, text="Input:", font=LABEL_FONT).pack(anchor="w", padx=20)

input_frame = ttk.Frame(root)
input_frame.pack(padx=20, pady=5, fill=tk.X)

input_text = tk.Text(
    input_frame,
    height=6,
    width=70,
    font=TEXT_FONT,
    relief=tk.SOLID,
    borderwidth=1
)
input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Convert and Clear Button
button_frame = ttk.Frame(root)
button_frame.pack(pady=15)

convert_button = ttk.Button(
    button_frame,
    text="Convert",
    command=convert_action,
    width=18
)
convert_button.pack(side=tk.LEFT, padx=10)

clear_button = ttk.Button(
    button_frame,
    text="Clear",
    command=clear_action,
    width=18
)
clear_button.pack(side=tk.LEFT, padx=10)

copy_button = ttk.Button(
    button_frame,
    text="Copy Output",
    command=copy_action,
    width=18
)
copy_button.pack(side=tk.LEFT, padx=10)

# Output
ttk.Label(root, text="Output:",font=LABEL_FONT).pack(anchor="w", padx=20)

output_frame = ttk.Frame(root)
output_frame.pack(padx=20, pady=5, fill=tk.X)

output_text = tk.Text(
    output_frame,
    height=6,
    width=70,
    font=TEXT_FONT,
    relief=tk.SOLID,
    borderwidth=1,
    state="disabled"
)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

output_scroll = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=output_text.yview)
output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=output_scroll.set)

# Start the Application
root.mainloop()