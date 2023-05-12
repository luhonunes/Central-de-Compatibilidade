#Inicia o Programa com uma saudação
print('Olá, seja Bem Vindo(a) a Central de Compatibilidade!')

lista_candidatos = [] #criando lista vazia para o cadastro de candidatos

#Entrando no Menu Principal
print('*MENU PRINCIPAL*')

while True:  #Loop Principal
    
    print('Selecione uma opção: \n1 - Cadastrar novo candidato: \n2 - Ver lista de candidatos: \n3 - Buscar candidato por nota: \n4 - Excluir candidato: \n5 - Sair do programa: \n')
    opcao = input('Digite o número da opção desejada: ') #Opçãoes 1, 2 , 3, 4, 5 (caso nao seja digitado nenhuma delas, é enviado mensagem de erro e voltam as opçoes inicial)
   
    if opcao == '1': #Cadastrar novo candidato
        nome = input('Digite o nome do candidato (ou 0 para voltar ao Menu Inicial): ')  
        e = (input('Digite a nota do candidato na entrevista: '))
        t = (input('Digite a nota do candidato no teste teórico: '))
        p = (input('Digite a nota do candidato no teste prático: '))
        s = (input('Digite a nota do candidato na avaliação de soft skills: '))
        lista_candidatos.append({'nome': nome, 'e': e, 't': t, 'p': p, 's': s}) #Adicionando Candidatos a Lista
        print(f'Candidato {nome} cadastrado com sucesso!') #Mensagem de confirmação
        
    elif opcao == '2': #Ver lista de candidato
        print('Lista de candidatos:')
        for candidato in lista_candidatos: #percorre a lista e exibe os candidatos em lista e formatado
            print(f"{candidato['nome']} - e{candidato['e']}_t{candidato['t']}_p{candidato['p']}_s{candidato['s']}")
            
    elif opcao == '3': #Buscar candidato por nota, usando as notas digitadas a seguir como parametros
        nota_e = int(input('Digite a nota mínima da entrevista: '))   
        nota_t = int(input('Digite a nota mínima do teste teórico: '))
        nota_p = int(input('Digite a nota mínima do teste prático: '))
        nota_s = int(input('Digite a nota mínima da avaliação de soft skills: '))
            
        print('Candidatos Encontrados: ')
        
        candidatos_encontrados = [] #criando lista vazia para candidatos encontrados
        for candidato in lista_candidatos: #percorre a lista 
            notas = [candidato['e'], candidato['t'], candidato['p'], candidato['s']] #cria uma sublista para verificar as notas
            #converte a nota str em int
            nota_e_cand = int(notas[0])
            nota_t_cand = int(notas[1])
            nota_p_cand = int(notas[2])
            nota_s_cand = int(notas[3])
            #compara as notas com os parametros
            if nota_e_cand >= nota_e and nota_t_cand >= nota_t and nota_p_cand >= nota_p and nota_s_cand >= nota_s:
                #adiciona os candidatos selecionados a lista
                candidatos_encontrados.append({'nome':candidato ['nome'],'e':nota_e_cand,'t':nota_t_cand,'p':nota_p_cand,'s':nota_s_cand})
               
        for candidato in candidatos_encontrados:  #percorre a lista e exibe os candidatos selecionados em lista e formatado 
            print(f"{candidato['nome']} - e{candidato['e']}_t{candidato['t']}_p{candidato['p']}_s{candidato['s']}")
    
    elif opcao == '4': #Excluir candidato
        nome_candidato = input('Digite o nome do candidato a ser excluído: ')
        for candidato in lista_candidatos: #percorre a lista 
            if candidato['nome'] == nome_candidato: #verifica se o nome esta na lista
                lista_candidatos.remove(candidato) #remove o candidato encontrado
                print(f"Candidato {nome_candidato} excluído com sucesso!") #confirma a exclusão
            else:
                print(f"Candidato {nome_candidato} não encontrado.")      #mensagem caso nao conste o nome do candidato na lista
                    
    elif opcao == '5': #Sair do programa
         while True:
            saida=input("Deseja sair da Central de Compatibilidade? (sim/nao):")
            if saida.lower () not in ['sim','nao']:
                print("Digite 'sim' para Sair ou 'nao' para retornar ao Menu Principal.")
                continue
            else:
                if saida == "sim":
                    print("\nFinalizando Central de Compatibilidade...\n")
                    exit()
                elif saida == "nao":
                    break  

    else: #Mensagem de erro caso nao seja digitada a opção correta
        print('Por favor, digite o número correspondente à opção desejada.')     