#================================
#FUNÇÃO 1 - CALCULA MÉDIA
#================================
def calcular_media(lista_notas):
    soma = sum(lista_notas)
    media = soma / len(lista_notas)
    return media

#================================
#FUNÇÃO 2 - VERIFICAR SITUAÇÃO
#================================
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


#=================================
#PROGRAMA PRINCIPAL
#=================================

# lista para armazenar todos os alunos
alunos = []

# quantidade de alunos
quantidade = int(input("Quantos alunos deseja cadastrar? "))

#===================================
#ENTRADA + PROCESSAMENTO
#===================================
for i in range(quantidade):
    print(f"\nAluno {i + 1}")

    nome = input("Digite o nome do aluno: ")

    notas = []

    for j in range(3):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)

    # 👉 AGORA DENTRO DO FOR (CORRETO)
    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)


#===================================
#SAÍDA DE DADOS
#===================================
print('\n===== RESULTADO FINAL =====')

for aluno in alunos:
    print("\n-----------------------")
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")
