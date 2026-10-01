def buscar_por_codigo(lista_objetos, codigo):
    for objeto in lista_objetos:
        if objeto["codigo"] == codigo:
            return objeto

    return None

def buscar_por_nome(lista_objetos, nome):
    resultados = []

    nome = nome.strip().lower()

    for objeto in lista_objetos:
        if nome in objeto["nome"].lower():
            resultados.append(objeto)

    return resultados

def buscar_por_categoria(lista_objetos, categoria):
    resultados = []

    categoria = categoria.strip().lower()

    for objeto in lista_objetos:
        if objeto["categoria"].lower() == categoria:
            resultados.append(objeto)

    return resultados

def buscar_por_local(lista_objetos, local):
    resultados = []

    local = local.strip().lower()

    for objeto in lista_objetos:
        if objeto["local"].lower() == local:
            resultados.append(objeto)
    return resultados

def buscar_por_tipo(lista_objetos, tipo):
    resultados = []

    tipo = tipo.strip().lower()

    for objeto in lista_objetos:
        if objeto["tipo"].lower() == tipo:
            resultados.append(objeto)
    return resultados

def buscar_por_status(lista_objetos, status):
    resultados = []

    status = status.strip().lower()

    for objeto in lista_objetos:
        if objeto["status"].lower() == status:
            resultados.append(objeto)
    return resultados