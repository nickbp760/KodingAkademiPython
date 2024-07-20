from tkinter import Tk, Entry, Button, END


root = Tk()
root.title("Calculator")

# Create entry widget for display
display = Entry(root, width=20, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Button texts
button_texts = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]


# Function to handle button clicks
def button_click(key):
    if key == '=':
        try:
            print(display.get())
            result = eval(display.get())
            display.delete(0, END)
            display.insert(END, str(result))
        except Exception:
            display.delete(0, END)
            display.insert(END, "Error")
    elif key == 'C':
        display.delete(0, END)
    else:
        display.insert(END, key)


# Create and place buttons
row = 1
col = 0
for button_text in button_texts:
    Button(root, text=button_text, width=8, height=2,
           command=lambda x=button_text: button_click(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
