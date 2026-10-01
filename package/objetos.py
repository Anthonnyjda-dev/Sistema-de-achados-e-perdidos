def gerar_codigo(lista_obejtos):
    """BLOCO QUE GERA O CODIGO DOS ITENS PERDIDOS"""
    if lista_obejtos == []:
        return 1

    maior_codigo = 0
    
    for objeto in lista_obejtos:
        if objeto['Codigo'] > maior_codigo:
         maior_codigo = objeto['Codigo']
    return maior_codigo + 1


def cadastrar_objeto(lista_objetos):
    """CADASTRA UM NOVO OBJETO NA LISTA"""
    novo_codigo = gerar_codigo(lista_objetos)
    nome = input('Digite o nome do objeto: ')
    categoria = input('Digite a categoria do objeto: ')
    descricao = input('Dê uma breve descrição do objeto: ')
    local = input('Informe o local que foi encontrado/perdido: ')
   
    tipo = input('Informe o tipo, perdido ou encontrado: ').lower()
    if tipo == 'perdido': #escolhas de tipo
        status = 'Procurando' #Atribuição de status
    elif tipo == 'encontrado':
        status = 'Disponível'
    else: 
        print('Tipo inválido')
        return 
    
    dia = int(input('Informe o dia: '))
    mes = int(input('Informe o mês: '))
    ano = int(input('Informe o ano: '))
    
    if dia < 1 or dia > 31:
        print('Dia inválido')
        return
    if mes < 1 or mes > 12:   #validação 
        print('Mês inválido')
        return 
    
    data = (dia, mes, ano)
    
    responsavel = input('Digite o  nome do responsável: ')
    
    novo_objeto = {
        'Codigo': novo_codigo,
        'Nome': nome,
        'Categoria': categoria,
        'Descrição': descricao,
        'Local': local,
        'Tipo': tipo,
        'Status': status,
        'Responsável': responsavel
    }
    
    lista_objetos.append(novo_objeto)
    return novo_objeto  

def localizar_por_codigo(lista_objetos, codigo_procurado):
    """LOCALIZAR UM OBJETO PELO SEU CÓDIGO"""
    for objeto in lista_objetos:
        if objeto['Codigo'] == codigo_procurado:
            return objeto
        
    return None