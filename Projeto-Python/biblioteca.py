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
    candidato_encontrado = False  # Variável para indicar se o candidato foi encontrado ou não
    
    for candidato in lista_candidatos:       
        if candidato['nome'] == nome: #Verifica se o nome consta na lista
            while True:
                excluir = input(f'Certeza que deseja excluir o candidato {nome}? (sim/nao):') #Mensagem de verificação
                print('-'*60)
                if excluir.lower () == 'sim': #verifica se o dado corresponde as opções
                    lista_candidatos.remove(candidato)  # remove candidato
                    print(f'Candidato {nome} excluído com sucesso!')  # mensagem de sucesso na exclusão
                    print('='* 60)
                elif excluir.lower() == 'nao':
                    print('='*60)
                else:
                    print(f"Opção Inválida. Digite 'sim' para excluir {nome} ou 'nao' para retornar ao Menu Principal.")  # mensagem caso o valor não corresponda
                    print('-'*60)
                    continue
                candidato_encontrado = True  # Indica que o candidato foi encontrado
                break  # Sai do loop após excluir o candidato

    if not candidato_encontrado:
        print(f'Candidato {nome} não encontrado')  # caso nome não for encontrado, retorna a informação
        print('-'*60)
        
#Função para verificar se o input pode ser convertido para int       
def verifica_numero (nota):
    while True:
        try:
            valor = int(input(nota))
            return valor
        except ValueError: #Mensagem de erro para valores inválidos
            print('Valor inválido para a nota do candidato. Por favor, digite um número inteiro.')

#Função para verificar se a lista de candidatos esta vazia            
def lista_vazia(lista):
    if len(lista) == 0: #Mensagem em caso de lista vazia
        print('A lista está vazia. Por favor, insira um novo candidato.')
        print('=' * 60)
        return True
    return False