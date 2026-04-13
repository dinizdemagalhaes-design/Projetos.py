#================================
#CLASSE ALUNO
#================================
class Aluno:

    #construtor (cria o aluno)
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    def calcular_media(self):
        return sum(self.notas)/ len(self.notas)
    
    #método para verificar situação
    def verificar_situacao(self):
        media = self.calcular_media()

        if media >=7:
            return "Aprovado"
        elif media >=5:
            return "Recuperação"
        else:
            return "Reprovado"
        

#====================================
#PROGRAMA INICIAL
#====================================

alunos = []
quantidade = int(input(f" Quantos alunos deseja cadastrar? "))

#=====================================
#ENTRADA DE DADOS
#=====================================
for i in range (quantidade):
    print(f"\n Aluno {i + 1}")

    nome = input("Digite o nome do aluno: ")

    notas = []
    for j in range (3):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)

    #cria objeto aluno
    aluno = Aluno(nome, notas)

    alunos.append(aluno)

#========================================
# SAÍDA DE DADOS
#========================================
print("\n===== RESULTADO FINAL =====")

for aluno in alunos:
    print("\n----------------------")
    print(f"Nome: {aluno.nome}")
    print(f"Notas: {aluno.notas}")
    print(f"Média: {aluno.calcular_media():.2f}")
    print(f"Situação: {aluno.verificar_situacao()}")

