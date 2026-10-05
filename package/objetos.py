from package.validacoes import validar_data

def gerar_codigo(lista_objetos, codigos_utilizados=None):
    """Gera um código maior que todos os códigos já utilizados."""
    maior_codigo = 0

    for objeto in lista_objetos:
        if objeto['codigo'] > maior_codigo:
            maior_codigo = objeto['codigo']

    if codigos_utilizados is not None:
        for codigo in codigos_utilizados:
            if codigo > maior_codigo:
                maior_codigo = codigo

    return maior_codigo + 1


def cadastrar_objeto(lista_objetos, codigos_utilizados=None):
    """CADASTRA UM NOVO OBJETO NA LISTA"""
    novo_codigo = gerar_codigo(lista_objetos, codigos_utilizados)
    nome = input('Digite o nome do objeto: ').strip()
    if nome == "":
        print('Nome vazio.')
        return

    categoria = input('Digite a categoria do objeto: ').strip()
    if categoria == "":
        print('Categoria vazia.')
        return
    descricao = input('Dê uma breve descrição do objeto: ').strip()
    if descricao == "":
        print('Descrição vazia.')
        return
    local = input('Informe o local que foi encontrado/perdido: ').strip()
    if local == "":
        print('Local vazio.')
        return

    tipo = input('Informe o tipo, perdido ou encontrado: ').lower().strip()
    if tipo == "":
        print('Tipo vazio.')
        return
    if tipo == 'perdido': #escolhas de tipo
        status = 'Procurando' #Atribuição de status
    elif tipo == 'encontrado':
        status = 'Disponível'
    else:
        print('Tipo inválido')
        return

    data = validar_data()

    responsavel = input('Digite o  nome do responsável: ').strip()
    
    if responsavel == '':
        print('Responsavel vazio.')
        return

    novo_objeto = {
        'codigo': novo_codigo,
        'nome': nome,
        'categoria': categoria,
        'descricao': descricao,
        'local': local,
        'data': data,
        'tipo': tipo,
        'status': status,
        'responsavel': responsavel
    }

    lista_objetos.append(novo_objeto)
    if codigos_utilizados is not None:
        codigos_utilizados.append(novo_codigo)
    return novo_objeto

def localizar_por_codigo(lista_objetos, codigo_procurado):
    """LOCALIZAR UM OBJETO PELO SEU CÓDIGO"""
    for objeto in lista_objetos:
        if objeto['codigo'] == codigo_procurado:
            return objeto

    return None

def listar_objetos(lista_objetos):
    if lista_objetos == []:
        print('Lista vazia.')
        return

    for objeto in lista_objetos:
        print('Código: ',objeto['codigo'])
        print('Nome: ', objeto['nome'])
        print('Categoria: ', objeto['categoria'])
        print('Descrição: ', objeto['descricao'])
        print('Local: ', objeto['local'])
        print('Data: ', objeto['data'])
        print('Tipo: ', objeto['tipo'])
        print('Status: ', objeto['status'])
        print('Responsável: ', objeto['responsavel'])
        print('-'*35)

def atualizar_objeto(lista_objetos, codigo_procurado):
    valor_busca = localizar_por_codigo(lista_objetos,codigo_procurado)
    if valor_busca is None:
        print('Valor não encontrado!')
        return

    opcao = input('O que deseja atualizar? 1:Categoria - 2:Status: ').strip()

    if opcao == '1':
        nova_categoria = input('Informe a nova categoria: ').strip()
        if nova_categoria == "":
            print('Categoria vazia')
            return
        valor_busca['categoria'] = nova_categoria
        print('Categoria atualizada: ', nova_categoria)

    elif opcao == '2':
        status = ('Procurando', 'Disponível')
        novo_status = input('Informe o novo status: ').strip().capitalize()
        if novo_status not in status:
            print('Status inválido.')
            return
        valor_busca['status'] = novo_status
        print('Status Atualizado: ', novo_status)

    else:
        print('Opção inválida.')
        return

def remover_objeto(lista_objetos, codigo_procurado):
    remover = localizar_por_codigo(lista_objetos, codigo_procurado)
    if remover is None:
        print('Valor não encontrado!')
        return
    remover_algo = input('Confirmar a remoção: (sim/não) ').strip().lower()

    if remover_algo == 'sim':
        lista_objetos.remove(remover)
        print('Objeto removido com sucesso!')
    elif remover_algo in ('nao', 'não'):
        print('A remoção foi cancelada.')
    else:
        print('Resposta inválida.')
