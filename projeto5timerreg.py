import tkinter  as tk

#Janela
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("600x400")

#Variáveis
tempo = 60
after_id = None

#Função contador
def atualizar_timer():
    global tempo, after_id

    if tempo > 0:
        tempo -= 1

        label_tempo.config(text=f"{tempo}seg")
        after_id =root.after(1000, atualizar_timer)

    else:
         label_tempo.config(text="Tempo acabou!")
         after_id =None

#Função Start
def iniciar():
    global after_id

    if after_id is None:
        atualizar_timer()

#Função reset
def resetar():
    global tempo, after_id

    if after_id is not None:
        root.after_cancel(after_id)

        tempo= 60
        label_tempo.config(text=f"{tempo}seg")
        after_id =None 


#Frame Superior
frame_topo =tk.Frame(root, bg="lightyellow")
frame_topo.place( relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)


#Frame Inferior
frame_inferior = tk.Frame(root, bg="lightyellow")
frame_inferior.place(relx=0.05, rely=0.78, relwidth=0.9, relheight=0.17)

#Label do tempo
label_tempo =tk.Label(frame_topo,text=f"{tempo} seg", font=("Arial", 40), bg="lightyellow", fg="green" )
label_tempo.place(relx=0.5, rely=0.5, anchor="center")


#Criar botao Start
button_start = tk.Button(frame_inferior, text="Start", command=iniciar,  bg="green", fg="white")
button_start.place(relx=0.25, rely=0.5, relwidth=0.3, relheight=0.7, anchor="center")

#Criar botao Reset
button_reset = tk.Button(frame_inferior, text="Reset", command=resetar, bg="red", fg="white")
button_reset.place(relx=0.75, rely=0.5, relwidth=0.3,relheight=0.7, anchor="center")


root.mainloop()
