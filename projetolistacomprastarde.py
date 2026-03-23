import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Lista")
root.geometry("400x500")
root.resizable(False, False)

# ---------------- DATA ----------------
lista = []

# ---------------- FUNCTIONS ----------------
def update_listbox():
    listbox_items.delete(0, tk.END)

    for index, item in enumerate(lista):
        listbox_items.insert(tk.END, f"{index} - {item}")


def insert_item():
    item = entry_item.get().strip()

    if item == "":
        messagebox.showwarning("Warning", "Please enter an item.")
    else:
        lista.append(item)
        entry_item.delete(0, tk.END)
        update_listbox()
        messagebox.showinfo("Success", "Item added successfully!")


def delete_item():
    try:
        selected_item = listbox_items.curselection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to delete.")
        else:
            index = selected_item[0]
            removed_item = lista.pop(index)
            update_listbox()
            messagebox.showinfo("Success", f"Item '{removed_item}' removed successfully!")

    except IndexError:
        messagebox.showerror("Error", "Invalid index.")


def list_items():
    if not lista:
        messagebox.showinfo("Shopping List", "The list is empty.")
    else:
        update_listbox()


# ---------------- TITLE ----------------
label_title = tk.Label(root, text="SHOPPING LIST", font=("Arial", 16, "bold"))
label_title.place(x=110, y=20)

# ---------------- ENTRY ----------------
label_item = tk.Label(root, text="Item:")
label_item.place(x=40, y=80)

entry_item = tk.Entry(root, font=("Arial", 12))
entry_item.place(x=90, y=78, width=220, height=28)

# ---------------- BUTTONS ----------------
button_insert = tk.Button(root, text="Insert", command=insert_item)
button_insert.place(x=40, y=130, width=90, height=35)

button_delete = tk.Button(root, text="Delete", command=delete_item)
button_delete.place(x=155, y=130, width=90, height=35)

button_list = tk.Button(root, text="List", command=list_items)
button_list.place(x=270, y=130, width=90, height=35)

# ---------------- LISTBOX ----------------
listbox_items = tk.Listbox(root, font=("Arial", 12))
listbox_items.place(x=40, y=190, width=320, height=230)


root.mainloop()
