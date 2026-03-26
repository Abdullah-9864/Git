import tkinter as tk

def add_data():
    data = entry.get()
    if data:
        listbox.insert(tk.END, data)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Data Lister")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add", command=add_data)
add_button.pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

root.mainloop()
