'''
https://www.youtube.com/watch?v=epDKamC-V-8
'''
import tkinter as tk

root = tk.Tk()
root.title('Simple app')

def add_to_list(event=None):
    text = entry.get()
    if text:
        text_list.insert(tk.END , text)
        entry.delete(0, tk.END)

frame = tk.Frame(root)
frame.grid(column=0, row=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)
entry.bind('<Return>', add_to_list)
# entry.bind('<Return>', lambda event: add_to_list()) # Alternative with lambda



entry_btn = tk.Button(frame, text='Add', command=add_to_list)
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(column=0, row=1)

root.mainloop()