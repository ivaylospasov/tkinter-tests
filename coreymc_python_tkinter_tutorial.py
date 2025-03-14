'''
https://www.youtube.com/watch?v=epDKamC-V-8
'''
import tkinter as tk

root = tk.Tk()
root.title('Simple app')

def on_click():
    # print('clicked')
    lbl.config(text='Button clicked')

lbl = tk.Label(root, text='Label 1')
lbl.grid(row=0, column=0)

btn = tk.Button(root, text='Button 1', command=on_click)
btn.grid(row=0, column=1)

root.mainloop()