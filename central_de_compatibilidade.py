#Função para buscar candidatos com as notas mínimas digitadas
def buscar_candidato(lista_candidatos, nota_e, nota_t, nota_p, nota_s):
    
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
    return candidatos_encontrados

#Função para excluir candidatos
def excluir_candidato(lista_candidatos, nome):
    for candidato in lista_candidatos:
        
        while True:
            if candidato['nome'] == nome: #Verifica se o nome consta na lista
                excluir=input(f'Certeza que deseja excluir o candidato {nome_candidato}? (sim/nao):') #Mensagem de verificação
                print('-'*60)
                if excluir.lower () not in ['sim','nao']: #verifica se o dado corresponde as opções
                    print(f"Opçao Inválida. Digite 'sim' para excluir {nome_candidato} ou 'nao' para retornar ao Menu Principal.") #mensagem caso o valor nao corresponda
                    print('-'*60)
                    continue
                else:
                    if excluir == 'sim':
                        lista_candidatos.remove(candidato) #remove candidato
                        print(f'Candidato {nome_candidato} excluído com sucesso!') #mensagem de sucesso na exclusão
                        print('='*60)
                        return 
                    elif excluir == 'nao':
                        print('='*60)
                        return
            else:
                print(f'Candidato {nome_candidato} não encontrado')#caso nome nao for encontrado, retorna a informação
                print('-'*60)
            return

#Inicia o Programa com uma saudação
print('\nOlá, seja Bem Vindo(a) a Central de Compatibilidade!')
print('-'*60)

lista_candidatos = [] #criando lista vazia para o cadastro de candidatos

while True:  #Loop Principal
    
    #Entrando no Menu Principal
    print('*MENU PRINCIPAL*')
    print('-'*60)
    
    print('Selecione uma opção: \n1 - Cadastrar novo candidato: \n2 - Ver lista de candidatos: \n3 - Buscar candidato por nota: \n4 - Excluir candidato: \n5 - Sair do programa: \n')
    print('-'*60)
    opcao = input('Digite o número da opção desejada: ') #Opçãoes 1, 2 , 3, 4, 5 (caso nao seja digitado nenhuma delas, é enviado mensagem de erro e voltam as opçoes inicial)
    print('='*60)
    
    if opcao == '1': #Cadastrar novo candidato
        
        while True:
            nome = input('Digite o nome do candidato (ou 0 para voltar ao Menu Inicial): ')
            print('='*60)
            if nome == '0': #confirma se o usuario quer retornar ao menu inicial
                break          
            e = (input('Digite a nota do candidato na entrevista: ')) 
            t = (input('Digite a nota do candidato no teste teórico: '))
            p = (input('Digite a nota do candidato no teste prático: '))
            s = (input('Digite a nota do candidato na avaliação de soft skills: '))
            print('-'*60)
            try: #Verifica se o valor inserido pode ser convertido para um número inteiro
                e = int(e)
                t = int(t)
                p = int(p)
                s = int(s)
            except: # Exibe mensagem caso algum valor digitado nao seja o desejado
                print('Valor inválido para a nota do candidato. Por favor, digite um número inteiro.')
                print('-'*60)
                continue
            lista_candidatos.append({'nome': nome, 'e': e, 't': t, 'p': p, 's': s}) #Adicionando Candidatos a Lista
            print(f'Candidato {nome} cadastrado com sucesso!') #Mensagem de confirmação
            print('-'*60)
            
    elif opcao == '2': #Ver lista de candidato
        
        if len(lista_candidatos) == 0: #Verificação de lista vazia
            print ('A lista está vazia, por favor insira um novo candidato.')
            print('='*60)
        else:
            print('Lista de candidatos:')
            for candidato in lista_candidatos: #percorre a lista e exibe os candidatos em lista e formatado
                print(f"{candidato['nome']} - e{candidato['e']}_t{candidato['t']}_p{candidato['p']}_s{candidato['s']}")
            print('='*60)
            
    elif opcao == '3': #Buscar candidato por nota, usando as notas digitadas a seguir como parametros
        
        if len(lista_candidatos) == 0: #Verificação de lista vazia
            print ('A lista está vazia, por favor insira um novo candidato.')
            print('='*60)
        else:
            while True:
                nota_e = (input('Digite a nota mínima da entrevista: '))   
                nota_t = (input('Digite a nota mínima do teste teórico: '))
                nota_p = (input('Digite a nota mínima do teste prático: '))
                nota_s = (input('Digite a nota mínima da avaliação de soft skills: '))
                print('-'*60)
                
                try: #Verifica se o valor inserido pode ser convertido para um número inteiro
                    nota_e = int(nota_e)
                    nota_t = int(nota_t)
                    nota_p = int(nota_p)
                    nota_s = int(nota_s)    
                except: # Exibe mensagem caso algum valor digitado nao seja o desejado
                    print('Valor inválido para a nota do candidato. Por favor, digite um número inteiro.')
                    print('-'*60)
                    continue  
                print('Candidatos Encontrados: ')
                candidatos_encontrados=buscar_candidato(lista_candidatos, nota_e, nota_t, nota_p, nota_s) #Chamando a função Buscar candidatos
                if len(candidatos_encontrados) == 0: #Verifica se a lista retornada é vazia
                    print ('Nenhum candidado encontrado com as notas mínimas inseridas') #Informa caso a lista esteja vazia, que nao tem nenhum candidato encontrado
                else:
                    for candidato in candidatos_encontrados:  #percorre a lista e exibe os candidatos selecionados em lista e formatado 
                        print(f"{candidato['nome']} - e{candidato['e']}_t{candidato['t']}_p{candidato['p']}_s{candidato['s']}")
                print('='*60)
                break
            
    elif opcao == '4': #Excluir candidato
        
        if len(lista_candidatos) == 0: #Verificação de lista vazia
            print ('A lista está vazia, por favor insira um novo candidato.')
            print('='*60)
        else:
            while True:
                nome_candidato = input('Digite o nome do candidato a ser excluído (ou 0 para voltar ao Menu Inicial): ')
                if nome_candidato == '0': #confirma se o usuario quer retornar ao menu inicial
                    print('='*60)
                    break
                else:
                    excluir_candidato(lista_candidatos, nome_candidato)   #Chamando a função Excluir candidato
                break
                
    elif opcao == '5': #Sair do programa
        
        while True:
            saida=input('Deseja sair da Central de Compatibilidade? (sim/nao):') #Mensagem de verificação
            if saida.lower () not in ['sim','nao']: #verifica se o dado corresponde as opções
                print("Opçao Inválida. Digite 'sim' para Sair ou 'nao' para retornar ao Menu Principal.") #mensagem caso o valor nao corresponda
                print('-'*60)
                continue
            else:
                if saida == 'sim':
                    print('\nFinalizando Central de Compatibilidade...\n') #Mensagens de Finalização
                    print( 'Obrigado por utilizar nosso Sistema!')
                    print('='*60)
                    exit()
                elif saida == 'nao':
                    print('='*60)
                    break  

    else: #Mensagem de erro caso nao seja digitada a opção correta
        print('O valor digitado não corresponde a uma opção válida, tente novamente.')     
        print('='*60)