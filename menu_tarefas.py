tarefas = []

def cadastrar_tarefa():
    titulo = input('Qual tarefa deseja cadastrar? ').strip()
    prioridade = input('Qual prioridade da tarefa? ')
    situacao = 'pendente'
    tarefas.append(titulo) 
    tarefas.append(prioridade)
    tarefas.append(situacao)
    print(f'Sua tarefa {titulo} foi cadastrada com sucesso!')

def listar_tarefa():
    numero_tarefa = 1
    for i in range(0, len(tarefas), 3):
        titulo = tarefas[i]
        prioridade = tarefas[i+1]
        situacao = tarefas[i+2]
        print(f'{numero_tarefa}. Tarefa: {titulo} | Prioridade: {prioridade} | Situação: {situacao}')
        numero_tarefa += 1

def atualizar_situacao():
    if not tarefas:
        print("Não há tarefas para atualizar.")
        return

    try:
       
        numero = int(input('Digite o número da tarefa que deseja atualizar: ')) 
        
        
        indice_situacao = (numero - 1) * 3 + 2
        
        
        if indice_situacao < len(tarefas) and numero > 0:
            nova_situacao = input("Digite a nova situação (Ex: concluida, em andamento): ").strip()
            
            
            tarefas[indice_situacao] = nova_situacao
            
            
            titulo_tarefa = tarefas[indice_situacao - 2]
            print(f'A situação da tarefa "{titulo_tarefa}" foi atualizada para: {nova_situacao}!')
        else:
            print("Número de tarefa inválido!")
            
    except ValueError:
        print("Por favor, digite um número inteiro válido.") 

def menu():

    while True:
        print("\n1 - Cadastrar tarefa ")
        print("2 - Listar tarefas")
        print("3 - Atualizar situação")
        print("4 - Encerrar sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefa()    
        elif opcao == "3":
            atualizar_situacao()    
        elif opcao == "4":
            print("Sistema encerrado")
            break    

menu()  