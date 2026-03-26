import tkinter  as tk
from tkinter import messagebox

#Janela Principal
root = tk.Tk()
root.title("To-Do List") 
root.geometry("400x500")
root.config(bg="Grey") 
root.resizable( True, True)

#Tasks
tasks =[]
task_y = 0.3

#Function
def update_counter():
    total=len(tasks)
    completed = 0

    for item in tasks:
        if item["var"].get():
            completed += 1
    counter_label.config(text=f"Total: {total} | Done: {completed}")

def add_tasks():
    global task_y

    text = task_entry.get().strip()

    if text == "":
        messagebox.showwarning("Warning", "Type a task first")
        return
        
    if task_y > 0.82:
        messagebox.showwarning("Warning", "No more space for tasks")
        return
    
    task_var= tk.BooleanVar()
    
    task_frame = tk.Frame(tasks_area, bg="#f4f4f4", bd=1, relief="solid")
    task_frame.place(relx=0.05, rely=task_y, relwidth=0.90, relheight=0.08)


    task_check =tk.Checkbutton(task_frame, text=text, variable=task_var,bg="#f4f4f4", font=("Arial", 12), anchor="w", command=update_task_style)
    task_check.place(relx=0.03, rely=0.15, relwidth=0.70, relheight=0.70)

    delete_button = tk.Button(task_frame, text="X", font=("Arial", 10, "bold"), bg="#ff7b7b", fg="white", command=lambda: delete_task(task_frame))
    delete_button.place(relx=0.82, rely=0.18, relwidth=0.12, relheight=0.55)

    task_data ={"text": text, "var": task_var, "frame": task_frame, "check": task_check, "button":delete_button, "y":task_y}
    tasks.append(task_data)
   
    task_entry.delete(0, tk.END)
    task_y += 0.10
    update_counter()

def update_task_style():
    for item in tasks:
        if item["var"].get():
            item["check"].config(fg="gray", font=("Arial", 12 ,"overstrike"))
        else:
            item["check"].comfig(fg="black", font=("Arial", 12))
    update_counter()

def delete_task (task_frame):
    global task_y

    for item in tasks:
        if item["frame"] == task_frame:
            item["frame"].destroy()
            tasks.remove(item)
            break

        reposition_tasks()
        update_counter

def delete_completed ():
    completed_tasks=[]

    for item in tasks:
        if item["var"].get():
            completed_tasks.append(item)

    for item in completed_tasks:
        item["var"].destroy()
        tasks.remove(item)


    reposition_tasks()
    update_counter()

def reposition_tasks():
    global task_y

    new_y =0.30

    for item in tasks:
        item["frame"].place_config(rely=new_y)
        item["y"] = new_y
        new_y+= 0.10

    task_y= new_y



#Main Frame
main_frame = tk.Frame(root,bg="#d2d197",bd=2,relief="solid")
main_frame.place(relx=0.03,rely=0.02,relwidth=0.94, relheight=0.96)

#Title
title_label = tk.Label(main_frame,text="To-Do List", font=("Arial", 20, "bold"),bg="white",fg="black")
title_label.place(relx=0.24,rely=0.04,relwidth=0.52,relheight=0.08)

#Entry
task_entry = tk.Entry(main_frame,font=("Arial", 12, "bold"))
task_entry. place (relx=0.08,rely=0.15,relwidth=0.62,relheight=0.07)

#Button
add_button = tk.Button(main_frame,text="Add", font=("Arial", 12,"bold"), bg="#90d1da", fg="black", command= add_tasks)
add_button. place(relx=0.73,rely=0.15,relwidth=0.18,relheight=0.07)

#Counter
counter_label = tk.Label(main_frame,text="Total: 0 | Done: 0",font=("Arial", 11, "bold"),bg="#d8d5a3", fg="black")
counter_label.place(relx=0.25, rely=0.24, relwidth=0.50, relheight=0.04)

#Tasks Area
tasks_area = tk.Frame(main_frame, bg="#d8d5a3" )
tasks_area.place(relx=0.03, rely=0.27, relwidth=0.94,relheight=0.60)

#Delete Completes Button
delete_completed_button = tk.Button(main_frame,text="Delete Completed",font=("Arial", 12, "bold"),bg="#e57373",fg="white",command=delete_completed)
delete_completed_button.place(relx=0.22, rely=0.90, relwidth=0.56, relheight=0.06)



root.mainloop()
