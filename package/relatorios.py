def valor_para_ordenar(objeto, campo):
    if campo == 'data':
        dia = objeto['data'][0]
        mes = objeto['data'][1]
        ano = objeto['data'][2]
        return (ano, mes, dia)
    return objeto[campo].lower()


def ordenar_objetos(lista_objetos, campo):
    campos_validos = ('nome', 'data', 'categoria', 'local', 'status')

    if campo not in campos_validos:
        print('Campo de ordenação inválido.')
        return []

    ordenada = []
    for objeto in lista_objetos:
        ordenada.append(objeto)

    for i in range(len(ordenada)):
        for j in range(len(ordenada) - 1 - i):
            if valor_para_ordenar(ordenada[j], campo) > valor_para_ordenar(ordenada[j + 1], campo):
                auxiliar = ordenada[j]
                ordenada[j] = ordenada[j + 1]
                ordenada[j + 1] = auxiliar

    return ordenada


def mostrar_estatisticas(lista_objetos):
    contagem = {
        'perdidos': 0,
        'encontrados': 0,
        'procurando': 0,
        'disponiveis': 0,
        'devolvidos': 0
    }

    for objeto in lista_objetos:
        if objeto['tipo'] == 'perdido':
            contagem['perdidos'] += 1
        elif objeto['tipo'] == 'encontrado':
            contagem['encontrados'] += 1

        if objeto['status'] == 'Procurando':
            contagem['procurando'] += 1
        elif objeto['status'] == 'Disponível':
            contagem['disponiveis'] += 1
        elif objeto['status'] == 'Devolvido':
            contagem['devolvidos'] += 1

    print('\n--- ESTATÍSTICAS ---')
    print('Total de objetos:', len(lista_objetos))
    print('Perdidos:', contagem['perdidos'])
    print('Encontrados:', contagem['encontrados'])
    print('Procurando:', contagem['procurando'])
    print('Disponíveis:', contagem['disponiveis'])
    print('Devolvidos:', contagem['devolvidos'])
    return contagem


def mostrar_por_categoria(lista_objetos):
    if lista_objetos == []:
        print('Nenhum objeto cadastrado.')
        return {}

    por_categoria = {}

    for objeto in lista_objetos:
        categoria = objeto['categoria'].strip().lower()
        if categoria in por_categoria:
            por_categoria[categoria] += 1
        else:
            por_categoria[categoria] = 1

    print('\n--- OBJETOS POR CATEGORIA ---')
    for categoria in por_categoria:
        print(categoria.capitalize(), ':', por_categoria[categoria])
    return por_categoria

def mostrar_devolucoes(lista_devolucoes):
    """Mostra todas as devoluções registradas."""
    if lista_devolucoes == []:
        print('Nenhuma devolução registrada.')
        return

    print('\n--- DEVOLUÇÕES ---')
    for devolucao in lista_devolucoes:
        print('Código do objeto:', devolucao['codigo_objeto'])
        print('Recebido por:', devolucao['recebedor'])
        print('Data:', devolucao['data'])
        print('-' * 35)