from package.validacoes import ler_texto, validar_data
from package.buscas import buscar_por_codigo

def registrar_devolucao(lista_objetos, lista_devolucoes, codigo):
    objeto = buscar_por_codigo(lista_objetos, codigo)

    if objeto is None:
        print("Objeto não encontrado.")
        return

    if objeto["status"] == "Devolvido":
        print("Esse objeto já foi devolvido")
        return

    nome_recebedor = ler_texto("Nome de quem recebeu: ")
    data_devolucao = validar_data()

    devolucao = {
        "codigo_objeto": codigo,
        "recebedor": nome_recebedor,
        "data": data_devolucao
    }
    lista_devolucoes.append(devolucao)

    objeto["status"] = "Devolvido"

    print("Devolução registrada com sucesso")