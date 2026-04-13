import tkinter as tk
from tkinter import messagebox


# =========================================
# LISTA PARA GUARDAR OS ALUNOS
# =========================================
alunos = []


# =========================================
# FUNÇÃO PARA CALCULAR MÉDIA
# =========================================
def calcular_media(notas):
    return sum(notas) / len(notas)


# =========================================
# FUNÇÃO PARA VERIFICAR SITUAÇÃO
# =========================================
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# =========================================
# FUNÇÃO PARA CADASTRAR ALUNO
# =========================================
def cadastrar_aluno():
    nome = entrada_nome.get()
    nota1 = entrada_nota1.get()
    nota2 = entrada_nota2.get()
    nota3 = entrada_nota3.get()

    # validar se os campos estão preenchidos
    if nome == "" or nota1 == "" or nota2 == "" or nota3 == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números nas notas.")
        return

    notas = [nota1, nota2, nota3]
    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso!")

    # limpar os campos
    entrada_nome.delete(0, tk.END)
    entrada_nota1.delete(0, tk.END)
    entrada_nota2.delete(0, tk.END)
    entrada_nota3.delete(0, tk.END)

    entrada_nome.focus()


# =========================================
# FUNÇÃO PARA MOSTRAR RESULTADOS
# =========================================
def mostrar_resultados():
    caixa_resultado.delete("1.0", tk.END)

    if len(alunos) == 0:
        caixa_resultado.insert(tk.END, "Nenhum aluno cadastrado.\n")
        return

    caixa_resultado.insert(tk.END, "===== RESULTADO FINAL =====\n\n")

    for i, aluno in enumerate(alunos, start=1):
        caixa_resultado.insert(tk.END, f"Aluno {i}\n")
        caixa_resultado.insert(tk.END, f"Nome: {aluno['nome']}\n")
        caixa_resultado.insert(tk.END, f"Notas: {aluno['notas']}\n")
        caixa_resultado.insert(tk.END, f"Média: {aluno['media']:.2f}\n")
        caixa_resultado.insert(tk.END, f"Situação: {aluno['situacao']}\n")
        caixa_resultado.insert(tk.END, "--------------------------\n")


# =========================================
# FUNÇÃO PARA LIMPAR RESULTADOS
# =========================================
def limpar_tudo():
    entrada_nome.delete(0, tk.END)
    entrada_nota1.delete(0, tk.END)
    entrada_nota2.delete(0, tk.END)
    entrada_nota3.delete(0, tk.END)
    caixa_resultado.delete("1.0", tk.END)
    alunos.clear()
    entrada_nome.focus()


# =========================================
# JANELA PRINCIPAL
# =========================================
janela = tk.Tk()
janela.title("Sistema de Controle de Notas")
janela.geometry("700x550")
janela.config(bg="#f2f2f2")


# =========================================
# TÍTULO
# =========================================
titulo = tk.Label(
    janela,
    text="Sistema de Controle de Notas",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2",
    fg="#1f1f1f"
)
titulo.pack(pady=15)


# =========================================
# FRAME DOS CAMPOS
# =========================================
frame_campos = tk.Frame(janela, bg="#f2f2f2")
frame_campos.pack(pady=10)


# nome
label_nome = tk.Label(frame_campos, text="Nome do aluno:", font=("Arial", 12), bg="#f2f2f2")
label_nome.grid(row=0, column=0, padx=10, pady=8, sticky="e")

entrada_nome = tk.Entry(frame_campos, font=("Arial", 12), width=25)
entrada_nome.grid(row=0, column=1, padx=10, pady=8)

# nota 1
label_nota1 = tk.Label(frame_campos, text="Nota 1:", font=("Arial", 12), bg="#f2f2f2")
label_nota1.grid(row=1, column=0, padx=10, pady=8, sticky="e")

entrada_nota1 = tk.Entry(frame_campos, font=("Arial", 12), width=10)
entrada_nota1.grid(row=1, column=1, padx=10, pady=8, sticky="w")

# nota 2
label_nota2 = tk.Label(frame_campos, text="Nota 2:", font=("Arial", 12), bg="#f2f2f2")
label_nota2.grid(row=2, column=0, padx=10, pady=8, sticky="e")

entrada_nota2 = tk.Entry(frame_campos, font=("Arial", 12), width=10)
entrada_nota2.grid(row=2, column=1, padx=10, pady=8, sticky="w")

# nota 3
label_nota3 = tk.Label(frame_campos, text="Nota 3:", font=("Arial", 12), bg="#f2f2f2")
label_nota3.grid(row=3, column=0, padx=10, pady=8, sticky="e")

entrada_nota3 = tk.Entry(frame_campos, font=("Arial", 12), width=10)
entrada_nota3.grid(row=3, column=1, padx=10, pady=8, sticky="w")


# =========================================
# FRAME DOS BOTÕES
# =========================================
frame_botoes = tk.Frame(janela, bg="#f2f2f2")
frame_botoes.pack(pady=15)

botao_cadastrar = tk.Button(
    frame_botoes,
    text="Cadastrar Aluno",
    font=("Arial", 12, "bold"),
    bg="#4caf50",
    fg="white",
    width=18,
    command=cadastrar_aluno
)
botao_cadastrar.grid(row=0, column=0, padx=10)

botao_mostrar = tk.Button(
    frame_botoes,
    text="Mostrar Resultados",
    font=("Arial", 12, "bold"),
    bg="#2196f3",
    fg="white",
    width=18,
    command=mostrar_resultados
)
botao_mostrar.grid(row=0, column=1, padx=10)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar Tudo",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=18,
    command=limpar_tudo
)
botao_limpar.grid(row=0, column=2, padx=10)


# =========================================
# ÁREA DE RESULTADO
# =========================================
caixa_resultado = tk.Text(janela, width=70, height=15, font=("Courier New", 11))
caixa_resultado.pack(pady=15)


# iniciar foco no nome
entrada_nome.focus()

# loop da janela
janela.mainloop()
