lista_clientes = []

while True:
    print("=====Lista de Clientes====")
    print("[1] Cadastrar  cliente")
    print("[2] Listar cliente")
    print("[3] Remover Cliente")
    print("[4] Sair")
    opção = input("escolha a opção:")

    if opção == "1":
       nome= input("Digite o nome do cliente: ").strip().upper()
       telefone = int(input("Digite o numero do celular: "))
       cliente =  {"nome": nome, "telefone": telefone}
       lista_clientes.append(cliente)
       print("Cadrasto de Cliente feito com sucesso")

    elif opção == "2":
        print("==== Lista de Clientes=====")
        for cliente in lista_clientes:
            print(f"{cliente["nome"]}| Telefone: {cliente["telefone"]}")

    elif opção =="4":
        print("Sair do Sistema")
        break

    else:
        print("Opção Inválida")
