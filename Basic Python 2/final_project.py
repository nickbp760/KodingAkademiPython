import tkinter as tk
from tkinter import messagebox
import os


def create_file():
    filename = filename_entry.get()
    content = input_entry.get("1.0", tk.END).strip()
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
            output_entry.config(state='normal')
            output_entry.delete("1.0", tk.END)
            output_entry.insert(tk.END, content)
            output_entry.config(state='disabled')
            input_entry.delete("1.0", tk.END)
            filename_desc.config(state='normal')
            filename_desc.delete(0, tk.END)
            filename_desc.insert(0, filename)
            filename_desc.config(state='readonly')
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
            output_entry.config(state='normal')
            output_entry.delete("1.0", tk.END)
            output_entry.insert(tk.END, content)
            output_entry.config(state='disabled')
            messagebox.showinfo("Success", f"File '{filename}' read successfully!")
            filename_desc.config(state='normal')
            filename_desc.delete(0, tk.END)
            filename_desc.insert(0, filename)
            filename_desc.config(state='readonly')
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
            filename_entry.delete(0, tk.END)
            input_entry.delete("1.0", tk.END)
            output_entry.config(state='normal')
            output_entry.delete("1.0", tk.END)
            output_entry.config(state='disabled')
            filename_desc.config(state='normal')
            filename_desc.delete(0, tk.END)
            filename_desc.config(state='readonly')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete file: {str(e)}")
    else:
        messagebox.showwarning("Warning", "File does not exist or no filename entered.")


def append_text():
    filename = filename_entry.get()
    current_filename = filename_desc.get()
    input_text = input_entry.get("1.0", tk.END).strip()
    current_output = output_entry.get("1.0", tk.END).strip()

    if not current_output:
        messagebox.showwarning("Warning", "Output is empty. Please read or create a file first.")
        return

    if filename != current_filename:
        messagebox.showwarning("Warning", "Filename doesn't match the current file. Please read the file first.")
        return

    if filename and os.path.exists(filename):
        try:
            with open(filename, 'a') as file:
                file.write("\n" + input_text)
            output_entry.config(state='normal')
            output_entry.insert(tk.END, "\n" + input_text)
            output_entry.config(state='disabled')
            input_entry.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Text appended successfully to file and output!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to append to file: {str(e)}")
    else:
        messagebox.showerror("File not found", "File not found. Please create a file first.")


def replace_text():
    current_filename = filename_desc.get()
    current_output = output_entry.get("1.0", tk.END).strip()

    filename = filename_entry.get()
    search_text = search_entry.get()
    replace_text = update_entry.get()

    if not current_output:
        messagebox.showwarning("Warning", "Output is empty. Please read or create a file first.")
        return

    if filename != current_filename:
        messagebox.showwarning("Warning", "Filename doesn't match the current file. Please read the file first.")
        return

    if not filename or not os.path.exists(filename):
        messagebox.showwarning("Warning", "File does not exist or no filename entered.")
        return

    try:
        with open(filename, 'r') as file:
            content = file.read()

        new_content = content.replace(search_text, replace_text)

        with open(filename, 'w') as file:
            file.write(new_content)

        output_entry.config(state='normal')
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, new_content)
        output_entry.config(state='disabled')

        messagebox.showinfo("Success", f"Text replaced and saved in file '{filename}'!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to replace text: {str(e)}")


root = tk.Tk()
root.title("File Creator")
root.geometry("600x300")

filename_label = tk.Label(root, text="Filename:")
filename_label.place(x=10, y=10)
filename_entry = tk.Entry(root, width=40)
filename_entry.place(x=10, y=30)

content_label = tk.Label(root, text="Input Content:")
content_label.place(x=10, y=60)
input_entry = tk.Text(root, width=28, height=5)
input_entry.place(x=10, y=80)

output_label = tk.Label(root, text="Output Content:")
output_label.place(x=350, y=60)
output_entry = tk.Text(root, width=28, height=5, state='disabled')
output_entry.place(x=350, y=80)

filename_desc_label = tk.Label(root, text="Current File:")
filename_desc_label.place(x=350, y=10)
filename_desc = tk.Entry(root, width=40, state='readonly')
filename_desc.place(x=350, y=30)

append_button = tk.Button(root, text="Append", command=append_text)
append_button.place(x=275, y=100)

create_button = tk.Button(root, text="Create File", command=create_file)
create_button.place(x=50, y=210)

read_button = tk.Button(root, text="Read File", command=read_file)
read_button.place(x=200, y=210)

delete_button = tk.Button(root, text="Delete File", command=delete_file)
delete_button.place(x=125, y=210)

search_label = tk.Label(root, text="Search:")
search_label.place(x=10, y=170)
search_entry = tk.Entry(root, width=20)
search_entry.place(x=60, y=170)

update_label = tk.Label(root, text="Update:")
update_label.place(x=200, y=170)
update_entry = tk.Entry(root, width=20)
update_entry.place(x=260, y=170)

replace_button = tk.Button(root, text="Replace", command=replace_text)
replace_button.place(x=420, y=165)

root.mainloop()
