#Importando Funções da Biblioteca
from biblioteca import *

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
            e = verifica_numero('Digite a nota do candidato na entrevista: ') 
            t = verifica_numero('Digite a nota do candidato no teste teórico: ')
            p = verifica_numero('Digite a nota do candidato no teste prático: ')
            s = verifica_numero('Digite a nota do candidato na avaliação de soft skills: ')
            print('-'*60)
            
            lista_candidatos.append({'nome': nome, 'e': e, 't': t, 'p': p, 's': s}) #Adicionando Candidatos a Lista
            print(f'Candidato {nome} cadastrado com sucesso!') #Mensagem de confirmação
            print('-'*60)
            
    elif opcao == '2': #Ver lista de candidato
        
        if lista_vazia(lista_candidatos):
            continue
        else:
            print('Lista de candidatos:')
            for candidato in lista_candidatos: #percorre a lista e exibe os candidatos em lista e formatado
                print(f"{candidato['nome']} - e{candidato['e']}_t{candidato['t']}_p{candidato['p']}_s{candidato['s']}")
            print('='*60)
            
    elif opcao == '3': #Buscar candidato por nota, usando as notas digitadas a seguir como parametros
        
        if lista_vazia(lista_candidatos):
            continue
        else:
            while True:
                nota_e = verifica_numero('Digite a nota mínima da entrevista: ')   
                nota_t = verifica_numero('Digite a nota mínima do teste teórico: ')
                nota_p = verifica_numero('Digite a nota mínima do teste prático: ')
                nota_s = verifica_numero('Digite a nota mínima da avaliação de soft skills: ')
                print('-'*60)
                
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
        
        if lista_vazia(lista_candidatos):
            continue
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
            if saida not in ['sim','nao']: #verifica se o dado corresponde as opções
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