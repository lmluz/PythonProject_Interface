import tkinter as tk

root = tk.Tk()
root.title('new app')
root.geometry('600x400')
root.configure(bg='#2b2b2b')

label = tk.Label(root, text='Dark Mode', bg='#2b2b2b', fg='white')
label.pack(pady=20)

button = tk.Button(root, text='oi', bg='#3c3f41', fg='white')
button.pack(pady=20)

root.mainloop()
root.destroy()