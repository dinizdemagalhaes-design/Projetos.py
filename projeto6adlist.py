import tkinter  as tk


#Janela Principal
root = tk.Tk()
root.title("To-Do List") 
root.geometry("400x500")
root.config(bg="Grey") 

#Tasks
tasks =[]
tasks_rely = 0.3

#Function
def add_tasks():
    global tasks_rely

    tasks_text = task_entry.get().strip()

    if tasks_text:
        task_var= tk.BooleanVar()

        task_check = tk.Checkbutton( main_frame,text=tasks_text,variable=task_var,font=("Arial", 12),bg="grey",anchor="w")
        task_check.place(relx=0.05,rely=tasks_rely,relwidth=0.80,relheight=0.06) 
        tasks.append((tasks_text, task_var, task_check))
        task_rely += 0.07
        task_entry.delete(0, tk.END) 

#Main Frame
main_frame = tk.Frame(root,bg="#d2d197",bd=1,relief="solid")
main_frame.place(relx=0.025,rely=0.02,relwidth=0.95, relheight=0.96)

#Title
title_label = tk.Label(main_frame,text="To-Do List", font=("Arial", 20, "bold"),bg="white",fg="black")
title_label.place(relx=0.28,rely=0.05,relwidth=0.44,relheight=0.08)

#Entry
task_entry = tk.Entry(main_frame,font=("Arial", 16, "bold"))
task_entry. place (relx=0.13,rely=0.15,relwidth=0.74,relheight=0.06)

#Button
add_button = tk.Button(main_frame,text="Adicionar Tarefa", font=("Arial", 14,"bold"), bg="#90d1da", fg="black", command= add_tasks)
add_button. place(relx=0.21,rely=0.23,relwidth=0.56,relheight=0.06)



root.mainloop()
