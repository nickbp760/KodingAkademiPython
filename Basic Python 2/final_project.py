import tkinter as tk
from tkinter import messagebox
import os


def create_file():
    filename = filename_entry.get()
    content = content_entry.get("1.0", tk.END).strip()
    if filename:
        if os.path.exists(filename):
            response = messagebox.askyesnocancel(
                "File Exist", "Replace file?\n Yes: Replace all content\nNo: Abort operation")
            if response is not True:
                return
        try:
            with open(filename, 'w') as file:
                file.write(content)
            messagebox.showinfo("Success", f"File '{filename}' created successfully with content!")
            filename_entry.delete(0, tk.END)  # Clear the filename entry field
            content_entry.delete("1.0", tk.END)  # Clear the content entry field
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create file: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a filename.")


def read_file():
    filename = filename_entry.get()
    if filename and os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
            output_entry.delete("1.0", tk.END)
            output_entry.insert(tk.END, content)
            messagebox.showinfo("Success", f"File '{filename}' read successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {str(e)}")
    else:
        messagebox.showwarning("Warning", "File does not exist or no filename entered.")


def delete_file():
    filename = filename_entry.get()
    if filename and os.path.exists(filename):
        try:
            os.remove(filename)
            messagebox.showinfo("Success", f"File '{filename}' deleted successfully!")
            filename_entry.delete(0, tk.END)  # Clear the filename entry field
            content_entry.delete("1.0", tk.END)  # Clear the content entry field
            output_entry.delete("1.0", tk.END)  # Clear the output entry field
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete file: {str(e)}")
    else:
        messagebox.showwarning("Warning", "File does not exist or no filename entered.")


# Create the main window
root = tk.Tk()
root.title("File Creator")
root.geometry("600x200")

# Create the filename entry field
filename_label = tk.Label(root, text="Filename:")
filename_label.place(x=10, y=10)
filename_entry = tk.Entry(root, width=40)
filename_entry.place(x=10, y=30)

# Create the content entry field
content_label = tk.Label(root, text="File Content:")
content_label.place(x=10, y=60)
content_entry = tk.Text(root, width=35, height=5)
content_entry.place(x=10, y=80)

# Create the output content field
output_label = tk.Label(root, text="Output Content:")
output_label.place(x=310, y=60)
output_entry = tk.Text(root, width=35, height=5)
output_entry.place(x=310, y=80)

# Create the buttons
create_button = tk.Button(root, text="Create File", command=create_file)
create_button.place(x=50, y=160)

read_button = tk.Button(root, text="Read File", command=read_file)
read_button.place(x=200, y=160)

delete_button = tk.Button(root, text="Delete File", command=delete_file)
delete_button.place(x=125, y=160)

# Start the Tkinter event loop
root.mainloop()
