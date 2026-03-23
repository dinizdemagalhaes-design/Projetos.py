import tkinter  as tk


root = tk.Tk()
root.title("Countdown Timer")
root.geometry("600x400")

#Variáveis
tempo = 60
after_id = None



#Função Contador
def atualizar_time():
    global tempo, after_id
    if tempo > 0:
        tempo -= 1

        label_tempo.config(text= F"{tempo} seg")
        after_id = root.after(1000, atualizar_time)
    
    else:
        label_tempo.config(text= "Tempo Acabou")
        after_id =None

#Função Start
def iniciar():
    global after_id

    if after_id is None:
        atualizar_time()

#Função Resetar
def resetar():
    global tempo, after_id
    if after_id is not None:
        root.after_cancel(after_id)

        tempo  = 60
        label_tempo.config(text=f"{tempo} seg")
        after_id = None

#Frame Superior
frame_topo =tk.Frame(root, bg="lightyellow")
frame_topo.place( relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)


#Frame Inferior
frame_inferior = tk.Frame(root, bg="lightyellow")
frame_inferior.place(relx=0.05, rely=0.78, relwidth=0.9, relheight=0.17)

#Label Tempo
label_tempo =tk.Label(frame_topo, text=f"{tempo} seg", font= ("Arial, 30"), bg="lightyellow", fg="green")
label_tempo.place(relx=0.5, rely=0.5,anchor="center")

#Criar botao Start
button = tk.Button(frame_inferior, text="Start", command=iniciar, font=("Arial, 16"), bg="green", fg="white")
button.place(relx=0.25, rely=0.5, relwidth=0.3, relheight=0.7, anchor="center")

#Criar botao Reset
button = tk.Button(frame_inferior, text="Reset", command=resetar,font=("Arial, 16"), bg="red", fg="white")
button.place(relx=0.75, rely=0.5, relwidth=0.3, relheight=0.7, anchor="center")


root.mainloop()
root.mainloop()
